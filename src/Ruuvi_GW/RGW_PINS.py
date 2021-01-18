from micropython import const

RB_BUTTON_RESET_PIN = const(35)

# Ruuvi GW BUS Pins
RB_GWBUS_1      =  const(5)
RB_GWBUS_2      =  const(17)
RB_GWBUS_3      =  const(36)
RB_GWBUS_4      =  const(37)
RB_GWBUS_5      =  const(38)
RB_GWBUS_LNA    =  const(4)

# Ruuvi GW Ethernet Pins
RB_GWETH_MDIO           = const(18)
RB_GWETH_TXD0           = const(19)
RB_GWETH_TXEN           = const(21)
RB_GWETH_TXD1           = const(22)
RB_GWETH_MDC            = const(23)
RB_GWETH_RXD0           = const(25)
RB_GWETH_RXD1           = const(26)
RB_GWETH_CRS_DV         = const(27)
RB_GWETH_ENABLE_ETH     = const(2)

# SWD Pins for nRF52
NRF52_GPIO_SWD_CLK  = const(15)
NRF52_GPIO_SWD_IO   = const(16)
NRF52_GPIO_NRST     = const(17)

# Uart Pins
RB_UART_NRF2ESP  = RB_GWBUS_3    ## //!< UART NRF -> ESP
RB_UART_ESP2NRF  = RB_GWBUS_1    ## //!< UART ESP -> NRF
TXD_PIN = RB_UART_ESP2NRF
RXD_PIN = RB_UART_NRF2ESP

# LNA Pin and modes
RB_PA_CRX_PIN = RB_GWBUS_LNA
RB_PA_CRX_TX_MODE = const(0)
RB_PA_CRX_RX_MODE = const(1)

