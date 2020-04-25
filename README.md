# ruuvi.gateway.micropython
Micropython FW for the ESP32 on the Ruuvi Gateway

The prebuilt FW should be flashed onto the Ruuvi Gateway as this includes the frozen modules. It can be found on the Releases page.

```bash
pip install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/ruuviGW_v1_4_0.bin
```

No files are needed to be uploaded via Pymakr as on first boot they are created via a python script :)

To build your own version follow the instruction found at https://github.com/micropython/micropython then at https://github.com/micropython/micropython/tree/master/ports/esp32 to install the micropython build environment and prepare the ESP32 SDK.

Once ready place all the files into ~/micropython/port/esp32/modules
Note: exclude any files that do not end with .py, for example the README.md

The WiFi hot-spot SSID and password is set in wifimgr.py

Once connect navigate to 192.168.4.1 and connect to your WiFi network.

The device will then get connected to your WiFi and receive an IP from your router.

Check your router or the REPL in pymakr and you will see the assigned IP.

Once connected to your network again navigate to that IP in a web browser.

You will be able to configure the device from the web page.

### IO pins:

ESP32 | Function
--|--
22 | Reset button
23 | LED
4 | UART TX
5 | UART RX


# Note
I have not implemented the Ethernet adapter as I do not have the physical hardware yet.

WiFi managemer is based on: https://github.com/tayfunulu/WiFiManager
Web Server is can be found at: https://github.com/jczic/MicroWebSrv2#mws2-adddefaultpage
Web design is based on the "Responsive Side Menu" at: https://purecss.io/layouts/
