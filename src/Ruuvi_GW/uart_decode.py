try:
    from micropython import const
except:
    const = lambda x: x
import time
import Ruuvi_GW.uart_const as uart_const
from Ruuvi_GW.ruuvi_status import RE_SUCCESS, \
                            RE_ERROR_DATA_SIZE, \
                            RE_ERROR_INVALID_PARAM, \
                            RE_ERROR_NULL, \
                            RE_ERROR_ENCODING, \
                            RE_ERROR_DECODING, \
                            RE_ERROR_DECODING_LEN, \
                            RE_ERROR_DECODING_DELIMITER, \
                            RE_ERROR_DECODING_STX, \
                            RE_ERROR_DECODING_ETX, \
                            RE_ERROR_DECODING_CRC, \
                            RE_ERROR_DECODING_CMD, \
                            RE_ERROR_NOT_IMPLEMENTED

from binascii import hexlify

U16_LSB_MASK    = const(0x00FF)
U16_MSB_MASK    = const(0xFF00)
U16_MSB_OFFSET  = const(8)
U8_HALF_OFFSET  = const(4)
CMD_ACK_MASK    = const(0x000000ff)
I8_MIN          = const(-128)
I8_MAX          = const(127)
U8_OVERFLOW     = const(256)

def calculate_crc16(p_data, size, p_crc):
    i = 0
    crc = uart_const.RE_CA_CRC_DEFAULT

    if p_data == None or size == 0:
        crc = uart_const.RE_CA_CRC_INVALID
    else:
        if p_crc == None:
            crc = p_crc
        
        while i < size:
            crc  = (crc >> U16_MSB_OFFSET) | (crc << U16_MSB_OFFSET)
            crc ^= p_data[i]
            crc ^= (crc & U16_LSB_MASK) >> U8_HALF_OFFSET
            crc ^= (crc << U16_MSB_OFFSET) << U8_HALF_OFFSET
            crc ^= ( (crc & U16_LSB_MASK) << U8_HALF_OFFSET) << 1
            i += 1

    return crc

def add_crc16(buffer, written):
    crc16 = uart_const.RE_CA_CRC_INVALID
    p_crc = uart_const.RE_CA_CRC_DEFAULT
    crc16 = calculate_crc16 (buffer + uart_const.RE_CA_UART_STX_ETX_LEN,
                             written - uart_const.RE_CA_UART_STX_ETX_LEN, p_crc)

    if crc16 != uart_const.RE_CA_CRC_INVALID:
        written = written + 1
        buffer[ written] = crc16 & U16_LSB_MASK
        written = written + 1
        buffer[ written] = (crc16 & U16_MSB_MASK) >> U16_MSB_OFFSET

def check_crc(buffer, written):
    state = False
    crc16 = uart_const.RE_CA_CRC_INVALID
    p_crc = uart_const.RE_CA_CRC_DEFAULT
    in_crc = buffer[-3:-2]
    crc16 = calculate_crc16 (buffer,
                             written - uart_const.RE_CA_UART_STX_ETX_LEN, p_crc)

    if crc16 != uart_const.RE_CA_CRC_INVALID:
        if in_crc == crc16:
            state = True

    return state

def u8toi8(byte):
    rval = byte
    if byte > I8_MAX:
        rval -= U8_OVERFLOW

    return rval

def i8tou8 (byte):
    rval = 0
    if 0 > byte:
        rval = U8_OVERFLOW + byte
    else:
        rval =  byte

    return rval

def re_ca_uart_decode_adv_rprt(buffer):
    adv_len = buffer[uart_const.RE_CA_UART_LEN_INDEX]\
                        - uart_const.RE_CA_UART_MAC_BYTES\
                        - uart_const.RE_CA_UART_RSSI_BYTES\
                        - (uart_const.RE_CA_UART_MAXFIELDS) * uart_const.RE_CA_UART_DELIMITER_LEN
    if adv_len > uart_const.RE_CA_UART_ADV_BYTES:
        pass
    else:
        buf = hexlify(buffer).decode().upper()
        buf = buf.split("2C")
        mac = buf[0]
        mac = mac[6:]
        if len(buf[1]) == (2 * adv_len):
            if len(mac) == 12:
                rssi = u8toi8(int(buf[2], 16))
                return mac, { 'data' : buf[1], 'rssi': rssi}