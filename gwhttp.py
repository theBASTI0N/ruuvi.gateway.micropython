from machine import UART
import machine
import urequests
import ujson
import time
from binascii import hexlify
import _thread
from gc import mem_free, collect
import gwlogging
from gwled import slow_pulse

global MAC
MAC = str.upper(hexlify(machine.unique_id(),).decode())

global epoch
epoch = False

def time_stamp(time):
  return "{}-{:0>2d}-{:0>2d}{}{:0>2d}:{:0>2d}:{:0>2d}{}".format(time[0], time[1], time[2], "T", time[3], time[4], time[5], "Z")

def uart():
    uart = UART(2, 115200)
    uart.init(115200, bits=8, parity=0, stop=1, tx=4, rx=5)
    while True:
        pkt = uart.readline() # read up to 5 bytes
        if (pkt != None):
            pkt = str(pkt)
            pkt = pkt.upper()
            pkt = pkt[2:-4]
            pkt = pkt.split(",")

            try:
                if len(pkt[0]) == 12 and len(pkt[1]) > 6 and len(pkt[2]) >-3 and int(pkt[2]) <= 0:
                   if epoch:
                       flT = time() + 946684800
                   else:
                       flT= time_stamp(time.localtime())
                   m = {'ts' : flT,
                        'mac' : pkt[0],
                        'data': pkt[1],
                        'rssi': int(pkt[2])}
                   tags.insert(1, m)
                   if len(tags) > 20:
                       tags.pop()

                else:
                    # Malformed UART data
                    pass
            except:
                pass

def http_update():
    collect()
    up = time.ticks_ms() / 1000
    mFr= mem_free()
    data = {'Messages': Messages,
    'memFree' : mFr,
    'uptime': up}
    return data

def start(config, pyhtml):
    gwlogging.sendLog(gwlogging.INFO, "Starting HTTP", MOD)
    global tags
    tags = []
    if int(config['epoch']) == 1:
        epoch = True
    _thread.start_new_thread(uart, ())
    pyhtml.SetGlobalVar('GwMode', 0)
    pyhtml.SetGlobalVar('active', 1)
    global Messages
    Messages = 0
    while True:
        slow_pulse(3)
        time.sleep(10)
        tempT = tags
        tags = []
        flT= time_stamp(time.localtime())
        m = {'ts' : flT,
                        'mac' : MAC,
                        'tags': tempT}
        msgJson = ujson.dumps(m)
        urequests.post(config['host'], data = msgJson)
        Messages = Messages + 1
