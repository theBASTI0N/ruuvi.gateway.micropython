from micropython import const

RE_CA_UART_SET_FLTR_TAGS    = const(5) #//!< Set filter tags.
RE_CA_UART_SET_FLTR_ID      = const(6) #//!< Set manufacturer ID filter.
RE_CA_UART_SET_CODED_PHY    = const(7) #//!< Set coded PHY.
RE_CA_UART_SET_SCAN_1MB_PHY = const(8) #//!< Set scan 1MBbit/PHY.
RE_CA_UART_SET_EXT_PAYLOAD  = const(9) #//!< Set extended payload.
RE_CA_UART_SET_CH_37        = const(10) #//!< Set channel 37.
RE_CA_UART_SET_CH_38        = const(11) #//!< Set channel 38.
RE_CA_UART_SET_CH_39        = const(12) #//!< Set channel 39.
RE_CA_UART_SET_ALL          = const(15) #//!< Set all config.
RE_CA_UART_ADV_RPRT         = const(16) #//!< Advertisement report. ACK no need.
RE_CA_UART_DEVICE_ID        = const(17) #//!< Send device id. ACK no need.
RE_CA_UART_GET_DEVICE_ID    = const(24) #//!< Get device id. Expect RE_CA_UART_DEVICE_ID.
RE_CA_UART_ACK              = const(32) #//!< ACK

RE_CA_CRC_DEFAULT               = const(0xFFFF)
RE_CA_CRC_INVALID               = const(0)

RE_CA_ACK_OK                    = const(0)
RE_CA_ACK_ERROR                 = const(1)

RE_CA_BOOL_ENABLE               = const(1)
RE_CA_BOOL_DISABLE              = const(0)

RE_CA_UART_DEVICE_ID_BYTES      = const(8) # //!< Number of bytes in DEVICE_ID
RE_CA_UART_DEVICE_ADDR_BYTES    = const(8) # //!< Number of bytes in DEVICE_ADDR
RE_CA_UART_MAC_BYTES            = const(6) # //!< Number of bytes in MAC address
RE_CA_UART_ADV_BYTES            = const(31) # //!< Number of bytes in Advertisement. 
RE_CA_UART_RSSI_BYTES           = const(1) # //!< Number of bytes in RSSI report.

RE_CA_UART_STX                  = const(0xCA) # //!< Start UART Command. Not related to ASCII STX.
RE_CA_UART_ETX                  = const(0x0A) # //!< End UART Command, '\n'. Not related to ASCII ETX.
RE_CA_UART_RSSI_MAXLEN          = const(RE_CA_UART_RSSI_BYTES) # //!< i8.
CMD_IN_LEN                      = const(0) # //!< Command is not included in data length.

RE_CA_UART_MAC_MAXLEN           = const(RE_CA_UART_MAC_BYTES) # //!< Length of MAC in UART.
RE_CA_UART_ADV_MAXLEN           = const(RE_CA_UART_ADV_BYTES) # //!< Length of adv.
RE_CA_UART_ADV_FIELDS           = const(3)   # //!< On scan: mac, data, rssi.
RE_CA_UART_MAXFIELDS            = const(RE_CA_UART_ADV_FIELDS) # //!< Maximum delimited fields.
RE_CA_UART_PAYLOAD_MAX_LEN      = (RE_CA_UART_MAC_MAXLEN \
                                    + RE_CA_UART_ADV_MAXLEN \
                                    + RE_CA_UART_RSSI_MAXLEN \
                                    + RE_CA_UART_MAXFIELDS) # //!< data + delimiters
RE_CA_UART_FIELD_DELIMITER = const(0x2C) # //!< ','
RE_CA_UART_DELIMITER_LEN   = const(1)    # //!< 1 byte delimiter.
#/** @brief STX, LEN, CMD, Payload, ETX */
RE_CA_UART_TX_MAX_LEN = (RE_CA_UART_PAYLOAD_MAX_LEN + 4)

RE_CA_UART_BLE_NOFILTER = const(0x0000) # //!< Do not apply filter to ID.

RE_CA_UART_HEADER_SIZE   = const(3) # //!< STX + len + CMD
RE_CA_UART_CRC_SIZE      = const(2) # //!< STX + len + CMD
RE_CA_UART_STX_INDEX     = const(0) # //!< Position of stx byte.
RE_CA_UART_LEN_INDEX     = const(1) # //!< Position of length byte.
RE_CA_UART_CMD_INDEX     = const(2) # //!< Position of CMD byte.
RE_CA_UART_PAYLOAD_INDEX = const(3) # //!< Start of payload.

RE_CA_UART_CH39_BYTE     = const(4) # //!< Byte of channel 39, starting from 0.
RE_CA_UART_CH39_BIT      = const(7) # //!< Bit of channel 39, starting from 0.
RE_CA_UART_CH38_BYTE     = const(4) # //!< Byte of channel 38, starting from 0.
RE_CA_UART_CH38_BIT      = const(6) # //!< Bit of channel 38, starting from 0.
RE_CA_UART_CH37_BYTE     = const(4) # //!< Byte of channel 37, starting from 0.
RE_CA_UART_CH37_BIT      = const(5) # //!< Bit of channel 37, starting from 0.

RE_CA_UART_125KBPS_BIT   = const(0) # //!< Bit of 125kpbs modulation, starting from 0.
RE_CA_UART_1MBPS_BIT     = const(1) # //!< Bit of 125kpbs modulation, starting from 0.
RE_CA_UART_2MBPS_BIT     = const(2) # //!< Bit of 125kpbs modulation, starting from 0.

RE_CA_UART_CMD_SFLTR_LEN    = const(2) # //!< Length of filter set command payload.
RE_CA_UART_CMD_CFLTR_LEN    = const(0) # //!< Length of filter clear command payload. 
RE_CA_UART_CMD_CH_LEN       = const(5) # //!< Length of channel command payload. 
RE_CA_UART_CMD_PHY_LEN      = const(1) # //!< Length of phy command payload. 

RE_CA_UART_BOOL_BYTE        = const(0) # //!< Byte of bool params, starting from 0.
RE_CA_UART_BOOL_BIT         = const(0) # //!< Bit of bool params, starting from 0.

RE_CA_UART_ACK_CMD_BYTE     = const(1) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ACK_BYTE         = const(1) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ACK_BIT          = const(0) # //!< Bit of bool params, starting from 0.

RE_CA_UART_FLTR_ID_BYTE         = const(2) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_BOOL_BYTE        = const(1) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_FLTR_TAG_BIT     = const(0) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_CODED_PHY_BIT    = const(1) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_SCAN_PHY_BIT     = const(2) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_EXT_PLD_BIT      = const(3) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_CH_37_BIT        = const(4) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_CH_38_BIT        = const(5) # //!< Byte of bool params, starting from 0.
RE_CA_UART_ALL_CH_39_BIT        = const(6) # //!< Byte of bool params, starting from 0.

RE_CA_UART_STX_ETX_LEN          = const(1) # //!< Length of cmd with bool payload
RE_CA_UART_GET_DEVICE_ID_LEN    = const(0) # //!< Length of get device id payload
RE_CA_UART_DEVICE_ID_LEN        = const(8) # //!< Length of device id payload
RE_CA_UART_DEVICE_ADDR_LEN      = const(8) # //!< Length of device addr payload
RE_CA_UART_CMD_BOOL_LEN         = const(1) # //!< Length of cmd with bool payload
RE_CA_UART_CMD_FLTR_ID_LEN      = const(2) # //!< Length of cmd with bool payload
RE_CA_UART_CMD_ACK_LEN          = const(2) # //!< Length of cmd with bool payload
RE_CA_UART_CMD_ALL_BOOL_LEN     = const(1) # //!< Length of cmd with bool payload
RE_CA_UART_CMD_ALL_LEN          = (RE_CA_UART_CMD_ALL_BOOL_LEN + RE_CA_UART_CMD_FLTR_ID_LEN)
# //!< Length of all command payload

RE_CA_UART_BOOL_FIELDS          = const(1)
RE_CA_UART_ACK_FIELDS           = const(2)
RE_CA_UART_DEVICE_ID_FIELDS     = const(2)
RE_CA_UART_GET_DEVICE_ID_FIELDS = const(0)
RE_CA_UART_FLTR_ID_FIELDS       = const(1)
RE_CA_UART_ALL_FIELDS           = (RE_CA_UART_BOOL_FIELDS + RE_CA_UART_FLTR_ID_FIELDS)