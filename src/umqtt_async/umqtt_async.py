from .umqtt_constants import *

try:
    import uasyncio as asyncio
except:
    import asyncio
try:
    import usocket as socket
except:
    import socket
try:
    import ustruct as struct
except:
    import struct
try:
    from ubinascii import hexlify
except:
    from binascii import hexlify
try:
    from utime import ticks_ms, ticks_diff
except:
    from time import time
    def ticks_ms(): return int(round(time()*1000))
    def ticks_diff(time1, time2): return time1 - time2
try:
    from uerrno import EINPROGRESS, ETIMEDOUT
except:
    from errno import EINPROGRESS, ETIMEDOUT

app = "MQTT_AS"
version = "0.1.0"

class MQTTException(Exception):
    pass

class MQTTClient:
    def __init__(self, client_id=None, broker=None, port=DEFAULT_TCP_PORT, 
                user=None, password=None, keep_alive=DEFAULT_KEEP_ALIVE,
                debug=False):
        # Client
        self.is_connected   = False
        self.first_connection = False
        if client_id == None:
            import random
            self.client_id = "umqtt_async/" + str(random.randint(1, 1000))
        else:
            self.client_id  = client_id
        if broker == None:
            raise ValueError("Missing Broker information.")
        self.broker     = broker
        self.port       = port
        self.user       = user
        self.password   = password
        self.keep_alive = keep_alive
        self.debug      = debug

        # SSL
        self.ssl        = False
        self.certs      = {}

        # LWT
        self.lw_topic   = None
        self.lw_msg     = None
        self.lw_qos     = DEFAULT_QOS
        self.lw_retain  = False

        # Messages and Topics
        self.pid                    = 0
        self.unack_pid              = []
        self.last_message_sent      = 0
        self.last_message_received  = 0
        self.topics                 = []
        self.resend_attempts        = 2

        # Callbacks
        self.on_message_cb          = None
        self.on_connection_cb       = None
        self.on_disconnect_cb       = None
        self.on_publish_cb          = None
        self.on_subscribe_cb        = None
        self.on_unsubscribe_cb      = None

        # Async
        self.reader         = None
        self.writer         = None
        self.lock           = asyncio.Lock()
        self.loop           = asyncio.get_event_loop()
        
        # Allows Network status to be passed to client.
        self.network_status = False 

    def set_lwt(self, lw_topic=None, lw_msg=None, lw_qos=DEFAULT_QOS, lw_retain=False):
        if lw_topic == None:
            raise ValueError('LWT Topic Empty.')
        else:
            self.lw_topic = lw_topic
        self.lw_msg = lw_msg
        if lw_qos == 0 or lw_qos == 1:
            self.lw_qos = lw_qos
        else:
            self.lw_qos = 0
        if lw_retain == True or lw_retain == False:
            self.lw_retain = lw_retain
        else:
            self.lw_retain = False
    
    # Not yet supported
    def set_ssl(self, ssl=False, certs={}):
        self.ssl = ssl
        self.certs = certs

    def new_pid(self):
        self.pid += 1
        if self.pid >= 35535:
            self.pid = 1

    async def read(self, n):
        while self.reader:
            try:
                msg = await self.reader.read(n)
            except OSError as e:
                msg = None
                if e.args[0] != EINPROGRESS or e.args[0] != ETIMEDOUT:
                    raise
            if msg == b'':
                raise OSError(-1)
            if msg is not None:
                self.last_message_received = ticks_ms()
            return msg
        else:
            raise OSError(-1)

    async def send(self, message, length=0):
        if self.writer:
            self.writer.write(message)
            await self.writer.drain()
            self.last_message_sent = ticks_ms()
        else:
            raise OSError(-1)

    async def send_str(self, s):
        await self.send(struct.pack("!H", len(s)))
        if isinstance(s, str):
            await self.send(str.encode(s, "utf-8"))
        else:
            await self.send(s)
    
    async def recv_len(self):
        n = 0
        sh = 0
        while 1:
            res = await self.read(1)
            b = res[0]
            n |= (b & 0x7f) << sh
            if not b & 0x80:
                return n
            sh += 7

    async def connect(self, clean_session=True):
        if self.network_status:
            if not self.is_connected:
                self.reader, self.writer = await asyncio.open_connection(self.broker, self.port)
                premsg = bytearray([0x10])
                msg = MQTT_HDR_CONNECT
                msg[6] = clean_session << 1

                length = 12 + len(self.client_id)
                if self.user is not None:
                    length += 4 + len(self.user) + len(self.password)
                    msg[6] |= 0xC0
                if self.keep_alive:
                    msg[7] |= self.keep_alive >> 8
                    msg[8] |= self.keep_alive & 0x00FF
                if self.lw_topic:
                    length += 4 + len(self.lw_topic) + len(self.lw_msg)
                    msg[6] |= 0x4 | (self.lw_qos & 0x1) << 3 | (self.lw_qos & 0x2) << 3
                    msg[6] |= self.lw_retain << 5
                
                large = False
                if length > 0x7F:
                    large = True
                    while length > 0:
                        encoded_byte = length % 0x80
                        length = length // 0x80
                    # if there is more data to encode, set the top bit of the byte
                        if length > 0:
                            encoded_byte |= 0x80
                        premsg.append(encoded_byte)

                if large:
                    premsg.append(0x00)
                else:
                    premsg.append(length)
                    premsg.append(0x00)

                await self.send(premsg)
                await self.send(msg)
                await self.send_str(self.client_id)
                if self.lw_topic is not None:
                    await self.send_str(self.lw_topic)
                    await self.send_str(self.lw_msg)
                if self.user is not None:
                    await self.send_str(self.user)
                    await self.send_str(self.password)
                while True:
                    op = await self.check_for_message()
                    if op == 32:
                        rc = await self.read(3)
                        if rc[0] != 0x02 or rc[2] != 0x00:
                            if rc[2] == 0x01:
                                raise OSError("Connection Refused - Incorrect Protocol Version")
                            elif rc[2] == 0x02:
                                raise OSError("Connection Refused - ID Rejected")
                            elif rc[2] == 0x03:
                                raise OSError("Connection Refused - Server unavailable")
                            elif rc[2] == 0x04:
                                raise OSError("Connection Refused - Incorrect username/password")
                            elif rc[2] == 0x05:
                                raise OSError("Connection Refused - Unauthorised")
                            else:
                                raise OSError("Connection Failed - Unknown Reason")
                        self.is_connected = True
                        if not self.first_connection:
                            self.first_connection = True
                            self.loop.create_task(self.connection_handler())
                        result = rc[0] & 1
                        #if self.on_connect is not None:
                        #   self.on_connect(self, self.user_data, result, rc[2])
                        self.loop.create_task(self.message_handler())  # Tasks quit on connection fail.
                        self.loop.create_task(self.keep_alive_task())
                        if self.debug:
                            print(app, ": Connected to: ", self.broker)
                        if self.on_connection_cb is not None:
                            await self.on_connection_cb()
                        return result
        else:
            raise OSError("No Network Connection")

    async def check_for_message(self):
        res = await self.read(1)
        if res == b'':
            return None
        
        res = res[0]

        if res == MQTT_PINGRESP:
            ping_resp = await self.read(1)
            if ping_resp[0] != 0x00:
                raise OSError("PINGRESP not returned from broker.")
            else:
                if self.debug:
                    print(app, ": PINGRESP RECEIVED.")
            return res
        elif res == MQTT_PUBACK:
            if self.debug:
                print(app, ": Received: MQTT_PUBACK")
            sz = await self.read(1)
            if sz != b"\x02":
                raise OSError(-1)
            rcv_pid = await self.read(2)
            pid = rcv_pid[0] << 8 | rcv_pid[1]
            if pid == self.pid:
                if pid in self.unack_pid:
                    self.unack_pid.remove(pid)
                return pid
            else:
                raise OSError(-1)
        elif res == MQTT_SUBACK:
            if self.debug:
                print(app, ": Received: MQTT_SUBACK")
            resp = await self.read(4)
            if resp[3] == MQTT_FAILURE:
                raise OSError(-1)
            pid = resp[2] | (resp[1] << 8)
            if pid == self.pid:
                if pid in self.unack_pid:
                    self.unack_pid.remove(pid)
                return pid
            else:
                raise OSError(-1)
        elif res == MQTT_UNSUBACK:
            if self.debug:
                print(app, ": Received: MQTT_UNSUBACK")
            resp = await self.read(1)
            if resp[0] != 0x02:
                raise OSError(-1)
            rcv_pid = await self.read(2)
            pid = rcv_pid[0] << 8 | rcv_pid[1]
            if pid == self.pid:
                if pid in self.unack_pid:
                    self.unack_pid.remove(pid)
                return pid
            else:
                raise OSError(-1)
        elif res & 0xF0 != 0x30:
            return res
        elif res == MQTT_PUB:
            if self.debug:
                print(app, ": Received: MQTT_PUB")
            sz = await self.recv_len()
            topic_len = await self.read(2)
            topic_len = (topic_len[0] << 8) | topic_len[1]
            topic = await self.read(topic_len)
            topic = str(topic, "utf-8")
            sz -= topic_len + 2
            if res & 0x06:
                pid = await self.read(2)
                pid = pid[0] << 0x08 | pid[1]
                sz -= 0x02
            msg = await self.read(sz)
            if self.on_message_cb is not None:
                self.on_message_cb(topic, str(msg, "utf-8"))
            if res & 0x06 == MQTT_SUCCES_QOS2: # Requesting PUBACK
                pkt = MQTT_PUBACK_MES
                struct.pack_into("!H", pkt, 2, pid)
                async with self.lock:
                    await self.send(pkt)
            elif res & 6 == 4:
                raise OSError(-1)
        else:
            raise OSError(-1)

    async def ping(self):
        async with self.lock:
            if self.debug:
                print(app, ": Sending PINREQ")
            await self.send(MQTT_PINGREQ)

    async def message_handler(self):
        try:
            while self.is_connected:
                await self.check_for_message()
        except OSError:
            pass
        self.is_connected = False


    async def keep_alive_task(self):
        while self.is_connected:
            if ticks_diff(ticks_ms(), self.last_message_received) >= (self.keep_alive*1000/2):
                try:
                    await self.ping()
                except OSError:
                    break
            await asyncio.sleep(1)
        self.is_connected = False
    
    async def connection_handler(self):
        while self.first_connection:
            if self.is_connected:
                await asyncio.sleep(1)
            else:
                if not self.network_status:
                    await asyncio.sleep(1)
                else:
                    try:
                        await self.connect()
                    except:
                        pass

    async def subscribe(self, topic, qos=0):
        if self.network_status:
            if self.is_connected:
                if topic is None:
                    raise ValueError("Topic can not be None.")
                if not isinstance(topic, str):
                    raise ValueError("Subsribe: Topic must be a string.")
                if 0 <= qos >= 2:
                    raise ValueError("Invalid QOS")
                pkt = MQTT_SUB
                self.new_pid()
                self.unack_pid.append(self.pid)
                struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic) + 1, self.pid)
                
                async with self.lock:
                    await self.send(pkt)
                    await self.send_str(topic)
                    await self.send(qos.to_bytes(1, "little"))

                    attempt = 0
                    while True:
                        await asyncio.sleep(1)
                        if self.pid in self.unack_pid and attempt <= self.resend_attempts:
                            await self.send(pkt)
                            await self.send_str(topic)
                            await self.send(qos.to_bytes(1, "little"))
                            attempt+=1
                        else:
                            if self.on_subscribe_cb is not None:
                                self.on_subscribe_cb(topic, qos, self.pid)
                            self.topics.append(topic)
                            break
                
    async def unsubscribe(self, topic):
        if self.network_status:
            if self.is_connected:
                if topic not in self.topics:
                    raise OSError(
                        "Topic must be subscribed too, \
                            before attempting to unsubscribe.")
                packet_length_byte = (4 + len(topic)).to_bytes(1, "big")
                self.new_pid()
                packet_id_bytes = self.pid.to_bytes(2, "big")
                packet = MQTT_UNSUB + packet_length_byte + packet_id_bytes
                topic_size = len(topic).to_bytes(2, "big")
                packet += topic_size + str.encode(topic, "utf-8")
                self.unack_pid.append(self.pid)
                async with self.lock:
                    await self.send(packet)
                    if self.on_unsubscribe_cb is not None:
                        self.on_unsubscribe_cb(topic, self.pid)

                    while True:
                        await asyncio.sleep(1)
                        if self.pid in self.unack_pid:
                            await self.send(packet)
                        else:
                            if self.on_unsubscribe_cb is not None:
                                self.on_unsubscribe_cb(topic, self.pid)
                            self.topics.remove(topic)
                            break           

    async def publish(self, topic, msg, retain=False, qos=0):
        if self.network_status:
            if self.is_connected:
                if "+" in topic or "#" in topic:
                    raise OSError("Publish topic can not contain wildcards.")
                if msg is None:
                    raise ValueError("Message can not be None.")
                if 0 <= qos >= 2:
                    raise ValueError("Invalid QOS")
                if isinstance(msg, (int, float)):
                    msg = str(msg).encode("ascii")
                elif isinstance(msg, str):
                    msg = str(msg).encode("utf-8")
                else:
                    raise ValueError("Invalid message data type.")

                pkt_hdr = bytearray([MQTT_PUB | retain | qos << 1])
                pub_hdr_var = bytearray(struct.pack(">H", len(topic)))
                pub_hdr_var.extend(topic.encode("utf-8"))

                remaining_length = 2 + len(msg) + len(topic)
                if qos > 0:
                    self.new_pid()
                    remaining_length += 2
                    pub_hdr_var.append(0x00)
                    pub_hdr_var.append(self.pid)
                    self.unack_pid.append(self.pid)
                
                if remaining_length > 0x7F:
                    while remaining_length > 0:
                        encoded_byte = remaining_length % 0x80
                        remaining_length = remaining_length // 0x80
                        if remaining_length > 0:
                            encoded_byte |= 0x80
                        pkt_hdr.append(encoded_byte)
                else:
                    pkt_hdr.append(remaining_length)
                
                async with self.lock:
                    await self.send(pkt_hdr)
                    await self.send(pub_hdr_var)
                    await self.send(msg)
                    if self.on_publish_cb is not None:
                        self.on_publish_cb(topic, msg, self.pid)

                    if qos > 0:
                        attempt = 0
                        while True:
                            await asyncio.sleep(0.5)
                            if self.pid in self.unack_pid and attempt <= self.resend_attempts:
                                await self.send(pkt_hdr)
                                await self.send(pub_hdr_var)
                                await self.send(msg)
                                attempt+=1
                            else:
                                if self.on_publish_cb is not None:
                                    self.on_publish_cb(topic, msg, self.pid)
                                break

    async def disconnect(self):
        if self.network_status:
            if self.is_connected:
                async with self.lock:
                    await self.send(MQTT_DISCONNECT)
                self.is_connected = False
                self.writer.close()
                await self.writer.wait_closed()
                if self.on_disconnect_cb is not None:
                    self.on_disconnect_cb(ticks_ms())
