from micropython import const

RE_SUCCESS                   = const(0)
RE_ERROR_DATA_SIZE           = const(1 << 3)  #//!< Data size too large/small.
RE_ERROR_INVALID_PARAM       = const(1 << 4)  #//!< Invalid Parameter.
RE_ERROR_NULL                = const(1 << 11) #//!< Null Pointer.
RE_ERROR_ENCODING            = const(1 << 12) #//!< Data encoding failed.
RE_ERROR_DECODING            = const(1 << 13) #//!< Data decoding failed.
RE_ERROR_DECODING_LEN        = const(1 << 14) #//!< Data decoding len failed.
RE_ERROR_DECODING_DELIMITER  = const(1 << 15) #//!< Data decoding delimiter failed.
RE_ERROR_DECODING_STX        = const(1 << 16) #//!< Data decoding stx failed.
RE_ERROR_DECODING_ETX        = const(1 << 17) #//!< Data decoding etx failed.
RE_ERROR_DECODING_CRC        = const(1 << 18) #//!< Data decoding crc failed.
RE_ERROR_DECODING_CMD        = const(1 << 19) #//!< Data decoding cmd failed.
RE_ERROR_NOT_IMPLEMENTED     = const(1 << 24)   #//!< Not implemented yet.