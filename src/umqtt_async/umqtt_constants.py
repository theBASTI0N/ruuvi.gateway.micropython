try:
    from micropython import const
except:
    const = lambda x: x

DEFAULT_TCP_PORT    = const(1883)
DEFAULT_TLS_PORT    = const(8883)
DEFAULT_KEEP_ALIVE  = const(60)
DEFAULT_QOS         = const(0)

MQTT_MAX_TOPIC_LENGTH   = const(65536)

MQTT_PINGREQ    = b"\xc0\0"
MQTT_SUB        = bytearray(b"\x82\0\0\0")
MQTT_UNSUB      = b"\xA2"
MQTT_DISCONNECT = b"\xe0\0"
MQTT_PUBACK_MES = bytearray(b"\x40\x02\0\0")

MQTT_SUCCES_QOS0 = const(0x00)
MQTT_SUCCES_QOS1 = const(0x01)
MQTT_SUCCES_QOS2 = const(0x02)
MQTT_FAILURE     = const(0x80)

MQTT_PINGRESP   = const(0xD0)
MQTT_PUB        = const(0x30)
MQTT_PUBACK     = const(0x40)
MQTT_SUBACK     = const(0x90)
MQTT_UNSUBACK   = const(0xB0)

# Variable CONNECT header [MQTT 3.1.1]
MQTT_HDR_CONNECT = bytearray(b"\x04MQTT\x04\x00\0\0")
