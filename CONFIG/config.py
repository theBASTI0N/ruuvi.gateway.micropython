lan_config = {
    "enabled"   : 1,
    # Mode 0 = DHCP
    "mode"      : 0,
    # Ised if mode : 1
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
    "server"    : "http://webhook.site/fcc664cd-f1d7-4b89-8cac-fd27b6e4a461",
    # Port is only needed if not standard 80 for http or 443 for https
    "port"      : 80
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
    # In topic 1 ruuvi could remain and gw could change to node for example to distinguish hardware type
    "topic1"    : "ruuvi/gw",
    # In topic 2 house is the building and office is where the gateway is placed
    "topic2"    : "house/office",
    "decode"    : 1
}