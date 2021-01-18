import gc
import uos
from flashbdev import bdev

try:
    if bdev:
        uos.mount(bdev, "/")
except OSError:
    import inisetup

    vfs = inisetup.setup()


try:
    uos.stat('/main.py')
except OSError:
    with open("/main.py", "w") as f:
        f.write("""import ruuvi_main""")

try:
    uos.stat('config.py')
except OSError:
    with open('config.py', "w") as f:
        f.write("""
lan_config = {
    "enabled"   : 1,
    # Mode 0 = DHCP
    "mode"      : 0,
    # Not used if Mode = 0
    "ip"        : "192.168.8.2",
    "subnet"    : "255.255.255.0",
    "router"    : "192.168.8.1",
    "dns"       : "8.8.8.8"
}

wifi_config = {
    "enabled"   : 0,
    "ssid"      : "yourssid",
    "password"  : "yourpassword",
    "mode"      : 0,
    # Not used if Mode = 0
    "ip"        : "192.168.8.2",
    "subnet"    : "255.255.255.0",
    "router"    : "192.168.8.1",
    "dns"       : "8.8.8.8"
}

http_config = {
    "enabled"   : 0,
    # Server can include port with :port
    "server"    : "https://yourserver.com",
    "port"      : 443
}

mqtt_config = {
    "enabled"   : 1,
    "broker"    : "test.mosquitto.org",
    "port"      : 1883,
    "username"  : None,
    "password"  : None,
    "ca"        : None,
    "cert"      : None,
    "key"       : None,
    "topic1"    : "ruuvi_gw",
    "topic2"    : "house/office"
}""")

gc.collect()
