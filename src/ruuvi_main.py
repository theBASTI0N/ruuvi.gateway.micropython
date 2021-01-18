import _thread, ujson, network, uasyncio as asyncio
from ntptime import settime
import Ruuvi_GW.RGW_PINS as RGW_PINS
from beacondecoder.decoder import decode
from time import sleep, time
from machine import unique_id, Pin, UART
import Ruuvi_GW.time_manager as tm
from Ruuvi_GW.ruuvi_status import *
from config import mqtt_config, http_config, lan_config, wifi_config 
from binascii import hexlify
from gc import mem_free, collect
from Ruuvi_GW.uart_decode import re_ca_uart_decode_adv_rprt, check_crc
from Ruuvi_GW.uart_const import RE_CA_UART_STX_INDEX,        \
                        RE_CA_UART_PAYLOAD_MAX_LEN, \
                        RE_CA_UART_STX,             \
                        RE_CA_UART_ETX,             \
                        RE_CA_UART_CMD_INDEX,       \
                        RE_CA_UART_LEN_INDEX,       \
                        RE_CA_UART_HEADER_SIZE,     \
                        RE_CA_UART_ACK,             \
                        RE_CA_UART_SET_FLTR_ID,     \
                        RE_CA_UART_SET_ALL,         \
                        RE_CA_UART_DEVICE_ID,       \
                        RE_CA_UART_GET_DEVICE_ID,   \
                        RE_CA_UART_ADV_RPRT,        \
                        RE_CA_UART_SET_FLTR_TAGS,   \
                        RE_CA_UART_SET_CODED_PHY,   \
                        RE_CA_UART_SET_SCAN_1MB_PHY,\
                        RE_CA_UART_SET_EXT_PAYLOAD, \
                        RE_CA_UART_SET_CH_37,       \
                        RE_CA_UART_SET_CH_38,       \
                        RE_CA_UART_SET_CH_39

if mqtt_config.get('enabled'):
    from umqtt_async import MQTTClient
if http_config.get('enabled'):
    import urequests_async as requests

__version__ = "0.0.1"

#=================================================================================================
#==========================================Networking=============================================
#=================================================================================================


MDC_PIN = Pin(RGW_PINS.RB_GWETH_MDC)
MDIO_PIN = Pin(RGW_PINS.RB_GWETH_MDIO)
ETH_PWR_PIN = Pin(RGW_PINS.RB_GWETH_ENABLE_ETH)

def Connect_LAN():
    global lan
    lan = network.LAN(mdc = MDC_PIN, mdio = MDIO_PIN, power=ETH_PWR_PIN, phy_type = network.PHY_LAN8720, phy_addr=0)
    lan.active(1)
    if lan_config.get('mode'):
        lan.ifconfig(lan_config.get('ip'), lan_config.get('subnet'), lan_config.get('router'), lan_config.get('dns'))
        sleep(5)
    while lan.ifconfig()[0] == "0.0.0.0":
        sleep(1)
    settime()
    print("LAN Connected.")

def Connect_WIFI():
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_config.get('ssid'), wifi_config.get('password'))
        while not wlan.isconnected():
            pass
        if lan_config.get('mode'):
            wlan.ifconfig(wifi_config.get('ip'), wifi_config.get('subnet'), wifi_config.get('router'), wifi_config.get('dns'))
            sleep(5)
        while wlan.ifconfig()[0] == "0.0.0.0":
            sleep(1)
        settime()
    print('WiFi Connected.')

#=================================================================================================
#==========================================UART===================================================
#=================================================================================================

uart = UART(2, baudrate=115200, bits=8, stop=1, parity=0, tx=RGW_PINS.TXD_PIN, rx=RGW_PINS.RXD_PIN)

LIMIT = 30  
global reports
reports = {}

def add_report(m, r):
    if m in reports.keys():
        # Overwrites Previous Entry
        reports[m] = r
    else:
        if len(reports) < LIMIT:
            reports[m] = r
        else:
            # Discard New Entry
            pass

def rx_parse_task(buffer):
    # Sanity check buffer format
    if None == buffer:
        return RE_ERROR_NULL
    elif RE_CA_UART_STX != buffer[RE_CA_UART_STX_INDEX]:
        return RE_ERROR_DECODING_STX
    elif RE_CA_UART_ETX != buffer[-1]:
        return  RE_ERROR_DECODING_ETX
    #elif (check_crc(buffer, (buffer[RE_CA_UART_LEN_INDEX] + RE_CA_UART_HEADER_SIZE)) != True):
        #  return RE_ERROR_DECODING_CRC
    else:
        if buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_ADV_RPRT:
            mac, adv = re_ca_uart_decode_adv_rprt(buffer)
            #Bad packets should not be decoded and will respond with None
            if adv != None:
                adv['timestamp'] = tm.unix_time_stamp()
                add_report(mac, adv)        
                return RE_SUCCESS
            else:
                return RE_ERROR_DECODING
        elif buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_ACK:
            print("RE_CA_UART_ACK RX'd")
            return RE_ERROR_NOT_IMPLEMENTED
        elif buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_FLTR_ID:
            print("RE_CA_UART_SET_FLTR_ID RX'd")
            return RE_ERROR_NOT_IMPLEMENTED
        elif buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_ALL:
            print("RE_CA_UART_SET_ALL RX'd")
            return RE_ERROR_NOT_IMPLEMENTED
        elif buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_DEVICE_ID:
            print("RE_CA_UART_DEVICE_ID RX'd")
            return RE_ERROR_NOT_IMPLEMENTED
        elif buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_GET_DEVICE_ID:
            print("RE_CA_UART_GET_DEVICE_ID RX'd")
            return RE_ERROR_NOT_IMPLEMENTED
        elif    buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_FLTR_TAGS or \
                buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_CODED_PHY or \
                buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_SCAN_1MB_PHY or \
                buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_EXT_PAYLOAD or \
                buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_CH_37 or \
                buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_CH_38 or \
                buffer[RE_CA_UART_CMD_INDEX] == RE_CA_UART_SET_CH_39:
            print("Set CMD  RX'd")
            return RE_ERROR_NOT_IMPLEMENTED
        else:
            return RE_ERROR_NOT_IMPLEMENTED

def uart_rx():
    while True:
        pkt = uart.readline()
        if (pkt != None):
            try:
                rx_parse_task(pkt)
            except KeyboardInterrupt:
                break
            except:
                pass

def uart_tx(buffer):
    try:
        uart.write(buffer)
    except:
        pass

_thread.start_new_thread(uart_rx, ())

loop = asyncio.get_event_loop()

#=================================================================================================
#==========================================Endpoints==============================================
#=================================================================================================

global MAC
MAC = str.upper(hexlify(unique_id(),).decode())

async def create_mqtt():
    global mqtt
    mqtt = MQTTClient(broker=mqtt_config.get('broker'), port=mqtt_config.get('port'), user=mqtt_config.get('username'), password=mqtt_config.get('password'))
    mqtt.network_status = True  #Add a async task that would set this and periodically check conenction
    await mqtt.connect()
    global MQTT_BASE_TOPIC
    MQTT_BASE_TOPIC = mqtt_config.get('topic1') + "/" + MAC + "/" + mqtt_config.get('topic2') + "/"

MOD = "MAIN"

def start():
    print("Ruuvi GW Micropython Version: ", __version__)
    if lan_config.get('enabled'):
        print("Connecting LAN")
        Connect_LAN()
    elif wifi_config.get('enabled'):
        print("Connecting WiFi")
        Connect_WIFI()
    else:
        print("No Network Config")

async def endpoint_loop():
    if mqtt_config.get('enabled'):
        await create_mqtt()
    while True:
        collect()
        temp = reports.copy()
        reports.clear()
        if mqtt_config.get('enabled'):
            for i in temp:
                m = {'edgeMAC': MAC, 'timestamp' : temp[i]['timestamp'],
                            'mac' : i,
                            'data': temp[i]['data'],
                            'rssi': temp[i]['rssi']}
                if mqtt_config.get('decode'):
                    try:
                        m['decoded'] = decode(temp[i]['data'])
                    except:
                        pass
                msgJson = ujson.dumps(m)
                await mqtt.publish( MQTT_BASE_TOPIC + "beacon/" + i, msgJson )
        if http_config.get('enabled'):
            m = {
                'data' : {
                    'coordinates' : '',
                    'timestamp' : tm.unix_time_stamp(),
                    'gwmac' : MAC,
                    'tags' : temp
                }}
            await requests.post(http_config.get('server'), json=m)
            #print(m['data']['timestamp'], ": Message Sent")
        await asyncio.sleep(10)


start()

loop.create_task(endpoint_loop())
loop.run_forever()