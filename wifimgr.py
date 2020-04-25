import network
import json
import time
from binascii import hexlify
import machine

MAC = str.upper(hexlify(machine.unique_id(),).decode())
ap_ssid = "RuuviGW_" + MAC[-3:]
ap_password = "ruuviG@t3way"
ap_authmode = 3  # WPA2

NETWORK_PROFILES = 'wifi.json'

wlan_ap = network.WLAN(network.AP_IF)
wlan_sta = network.WLAN(network.STA_IF)

def get_connection():
    """return a working WLAN(STA_IF) instance or None"""

    # First check if there already is any connection:
    if wlan_sta.isconnected():
        return wlan_sta

    connected = False
    try:
        # ESP connecting to WiFi takes time, wait a bit and try again:
        time.sleep(3)
        if wlan_sta.isconnected():
            return wlan_sta

        # Read known network profiles from file
        profiles = read_wifi()

        # Search WiFis in range
        wlan_sta.active(True)
        networks = wlan_sta.scan()

        AUTHMODE = {0: "open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
        for ssid, bssid, channel, rssi, authmode, hidden in sorted(networks, key=lambda x: x[3], reverse=True):
            ssid = ssid.decode('utf-8')
            encrypted = authmode > 0
            print("ssid: %s chan: %d rssi: %d authmode: %s" % (ssid, channel, rssi, AUTHMODE.get(authmode, '?')))
            if encrypted:
                if ssid in profiles['ssid']:
                    connected = do_connect(profiles)
                else:
                    print("skipping unknown encrypted network")
            if connected:
                break

    except OSError as e:
        print("exception", str(e))

    # start web server for connection manager:
    if not connected:
        connected = start_ap()
    return wlan_sta if connected else None

def check_connection():
    # First check if there already is any connection:
    if wlan_sta.isconnected():
        return wlan_sta
    connected = False
    return connected

def read_wifi():
    with open(NETWORK_PROFILES) as f:
        profiles = json.load(f)
    return profiles

def write_wifi(profiles):
    with open(NETWORK_PROFILES, 'w') as f:
        json.dump(profiles, f)
    return True

def get_ip():
    return wlan_sta.ifconfig()

def do_connect(profiles):
    wlan_sta.active(True)
    if wlan_sta.isconnected():
        return None
    print('Trying to connect to %s...' % profiles['ssid'])
    wlan_sta.connect(profiles['ssid'], profiles['password'])
    for retry in range(100):
        connected = wlan_sta.isconnected()
        if connected:
            break
        time.sleep(0.1)
        print('.', end='')
    if connected:
        print('\nConnected. Network config: ', wlan_sta.ifconfig())
    else:
        print('\nFailed. Not Connected to: ' + profiles['ssid'])
    return connected

def do_scan():
    wlan_sta.active(True)
    ssids = sorted(ssid.decode('utf-8') for ssid, *_ in wlan_sta.scan())
    return ssids

def start_ap():
    try:
        wlan_sta.active(True)
        wlan_ap.active(True)
        wlan_ap.config(essid=ap_ssid, password=ap_password, authmode=ap_authmode)
        print('Connect to WiFi ssid ' + ap_ssid + ', default password: ' + ap_password)
        print('and access the Ruuvi GW via your favorite web browser at 192.168.4.1.')
        return True
    except:
        return False