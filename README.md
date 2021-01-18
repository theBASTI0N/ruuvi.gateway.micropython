# Introduction
Micropython FW for your Ruuvi Gateway's ESP32 module.

## Features
1. Continous UART reading
2. Asynchronous MQTT/HTTP endpoints
3. Both HTTP and MQTT can be used at the same time

## Known Issue
1. Currently no SSL support. (Awaiting a PR to be approved for Micropython)
2. Web Server removed due to memory/threading issue whilst using lan. Asynchronous web server might be used in the future.

# Flashing
The prebuilt FW should be flashed onto the Ruuvi Gateway as this includes the frozen modules. It can be found on the Releases page.

```bash
pip3 install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
# Assumes only on is present in Downloads
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/ruuviGW_v*
```

# Configuration
Configuration is done via a python file, which can be found in the CONFIG folder.

mpfshell can be used to upload this once it has been edited for your environment.

```bash
git clone https://github.com/theBASTI0N/ruuvi.gateway.micropython.git
cd ruuvi.gateway.micropython
cd CONFIG
pip3 install mpfshell
mpfshell
# May be different on you system. Use ls /dev/tty* to look at devices
open ttyUSB0
put config.py
repl
```

Once the file has been placed on the device either restart it, or press CTRL+D when in the REPL.
