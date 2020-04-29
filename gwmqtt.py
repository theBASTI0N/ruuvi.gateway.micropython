from machine import UART
import machine
from umqtt.robust import MQTTClient
import time
import ujson
import _thread
from binascii import hexlify
from gc import mem_free, collect
import decoder
import gwlogging
from gwled import fast_pulse, slow_pulse
from config_manager import write_gw, read_gw, write_cloud, read_cloud, write_sys, read_sys

global DISCONNECTED
DISCONNECTED = 0
global CONNECTING
CONNECTING = 1
global CONNECTED
CONNECTED = 2

global MAC
MAC = str.upper(hexlify(machine.unique_id(),).decode())

MOD = "MQTT"

def time_stamp(time):
  return "{}-{:0>2d}-{:0>2d}{}{:0>2d}:{:0>2d}:{:0>2d}{}".format(time[0], time[1], time[2], "T", time[3], time[4], time[5], "Z")

def sub_cb(topic, msg):
    t = topic.decode()
    m = ujson.loads(msg.decode())
    if t == (MAC + "/config/web"):
        if m['web'] == 1 or m['web']== 0:
            write_gw(m)
            clientH.publish( topic=MAC + "/reply", msg ="Web Setting Set. Will take affect on next reboot." )
        else:
            clientH.publish( topic=MAC + "/reply", msg ="Web Settings Invalid." )
    elif t == (MAC + "/config/cloud"):
        if m['mode'] == 0:
            #HTTP
            if 'host' in m and 'dble' in m and 'epoch' in m:
                write_cloud(m)
                clientH.publish( topic=MAC + "/reply", msg ="HTTP Settings Set. Will take affect on next reboot." )
            else:
                clientH.publish( topic=MAC + "/reply", msg ="HTTP Settings Invalid" )
        elif m['mode'] == 1:
            #MQTT
            if 'host' in m and 'port' in m and 'dble' in m and 'epoch' in m and 'topic1' in m and 'topic2' in  m:
                write_cloud(m)
                if 'username' not in m or 'password' not in m:
                    clientH.publish( topic=MAC + "/reply", msg ="MQTT Settings Set. Authentication may be missing. Will take affect on next reboot." )
                else:
                    clientH.publish( topic=MAC + "/reply", msg ="MQTT Settings Set. Will take affect on next reboot." )
            else:
                clientH.publish( topic=MAC + "/reply", msg ="MQTT Settings Invalid" )
    elif t == (MAC + "/config/syslog"):
        if 'host' in m and 'port' in m and 'tcp' in m and 'TZ' in m:
            write_sys(m)
        else:
            clientH.publish( topic=MAC + "/reply", msg ="SYSLOG Settings Settings invladi." )
    elif t == (MAC + "/config/get"):
        if m['data']== 0:
            temp = read_gw()
            temp['edgeMAC'] = MAC
            msgJson = ujson.dumps(temp)
            clientH.publish( topic=MAC + "/reply", msg =msgJson )
        elif m['data'] == 1:
            temp = read_cloud()
            temp['edgeMAC'] = MAC
            msgJson = ujson.dumps(temp)
            clientH.publish( topic=MAC + "/reply", msg =msgJson )
        elif m['data'] == 2:
            temp = read_sys()
            temp['edgeMAC'] = MAC
            msgJson = ujson.dumps(temp)
            clientH.publish( topic=MAC + "/reply", msg =msgJson )
        elif m['data'] == 3:
            temp = mqtt_update()
            temp['edgeMAC'] = MAC
            msgJson = ujson.dumps(temp)
            clientH.publish( topic=MAC + "/reply", msg =msgJson )
    elif t == (MAC + "/config/restart"):
        if str.upper(m['mac']) == MAC:
            temp = MAC + "Restartig in " + m['delay'] + "seconds."
            clientH.publish( topic=temp )
            time.sleep(m['delay'])
            machine.reset()

def mqttH(config):#HeartBeat client
    state = DISCONNECTED
    global clientH
    if config['username'] != "" and config['password'] != "":
        clientH = MQTTClient( MAC + "H", config['host'] ,user=config['username'], password=config['password'], port=int(config['port']), keepalive=30, ssl=False)
    else:
        clientH = MQTTClient( MAC + "H", config['host'], port=int(config['port']), keepalive=30, ssl=False)

    clientH.set_callback(sub_cb)

    while state != CONNECTED:
        try:
            state = CONNECTING
            clientH.connect()
            state = CONNECTED
        except:
            gwlogging.sendLog(gwlogging.INFO, "Could not establish MQTT-H connection", MOD)
            time.sleep(1)
    if state == CONNECTED:
        gwlogging.sendLog(gwlogging.INFO, "MQTT-H Connected", MOD)
        subTopic = "%s/config/#" % MAC
        clientH.subscribe(subTopic)
        gwlogging.sendLog(gwlogging.INFO, "MQTT-H Subscribed to: %s" % subTopic, MOD)


def heartbeat(epoch):
    global heartMessages
    heartMessages = 0
    counter = 0
    while True:
        clientH.check_msg()
        counter += 1
        time.sleep(0.5)
        if counter == 20: #about 10 seconds
            counter = 0
            collect()
            if epoch == 1:
                flT = time.time() + 946684800
            else:
                flT= time_stamp(time.localtime())
            up = time.ticks_ms() / 1000
            mFr= mem_free()
            m = {'edgeMAC': MAC, 'ts' : flT,
                'memFree' : mFr,
                'uptime': up}
            msgJson = ujson.dumps(m)
            clientH.publish( topic=TOPIC + "heartbeat", msg =msgJson )
            heartMessages = heartMessages + 1
            slow_pulse(2)


def mqttB(config):#HeartBeat client
    state = DISCONNECTED
    global clientB
    if config['username'] != "" and config['password'] != "":
        clientB = MQTTClient( MAC, config['host'] ,user=config['username'], password=config['password'], port=int(config['port']), keepalive=30, ssl=False)
    else:
        clientB = MQTTClient( MAC, config['host'] ,port=int(config['port']), keepalive=30, ssl=False)
    while state != CONNECTED:
        try:
            state = CONNECTING
            clientB.connect()
            state = CONNECTED
        except:
            gwlogging.sendLog(gwlogging.INFO, "Could not establish MQTT-BLE connection", MOD)
            time.sleep(1)
    if state == CONNECTED:
        gwlogging.sendLog(gwlogging.INFO, "MQTT-BLE Connected", MOD)

def uart(epoch, decode):
    global Messages
    Messages = 0
    uart = UART(2, 115200)
    uart.init(115200, bits=8, parity=0, stop=1, tx=4, rx=5)
    while True:
        pkt = uart.readline()
        if (pkt != None):
            pkt = str(pkt)
            pkt = pkt.upper()
            pkt = pkt[2:-4]
            pkt = pkt.split(",")

            try:
                if len(pkt[0]) == 12 and len(pkt[1]) > 6 and len(pkt[2]) >-3 and int(pkt[2]) <= 0:
                    if epoch:
                       flT = time.time() + 946684800
                    else:
                       flT= time_stamp(time.localtime())
                    m = {'edgeMAC': MAC, 'ts' : flT,
                        'mac' : pkt[0],
                        'data': pkt[1],
                        'rssi': int(pkt[2])}
                    if decode:
                        d = decoder.decode(pkt[1])
                        m.update(d)
                    msgJson = ujson.dumps(m)
                    clientB.publish( topic=TOPICble + "beacon/" + pkt[0], msg =msgJson )
                    Messages = Messages + 1
                else:
                    # Malformed UART data
                    pass
            except:
                pass

def mqtt_update():
    collect()
    up = time.ticks_ms() / 1000
    mFr= mem_free()
    data = {'Mode': MOD, 'active': active, 'Messages': Messages, 'heartMessages': heartMessages,
    'memFree' : mFr,
    'uptime': up}
    return data

def start(config):
    global active
    active = 0
    gwlogging.sendLog(gwlogging.INFO, "Starting MQTT", MOD)
    epoch = 0
    global TOPIC
    TOPIC = config['topic1'] + "/" + MAC + "/"
    global TOPICble
    TOPICble = TOPIC + config['topic2'] + "/"
    if int(config['epoch']) == 1:
        epoch = 1
    mqttH(config)
    _thread.start_new_thread(heartbeat, (epoch,)) #Start HeartBeat loop
    mqttB(config)
    active = 1
    uart(epoch, config['dble'])
