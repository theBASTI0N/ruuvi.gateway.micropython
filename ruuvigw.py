from MicroWebSrv2 import *
import _thread
import wifimgr
import config_manager
from requests import *
from time import localtime, sleep, time
from ntptime import settime
from machine import Pin, reset
import gc
import gwlogging
from primitives.pushbutton import Pushbutton
import uasyncio as asyncio
from gwled import slow_pulse, fast_pulse

resetVal = None

try:
    GW_CONFIG = config_manager.read_gw()
except:
    GW_CONFIG = None

try:
    CLOUD_CONFIG = config_manager.read_cloud()
except:
    CLOUD_CONFIG = None


async def double_press():
    gwlogging.sendLog(gwlogging.INFO, "Double Press Detected", MOD)
    if wifimgr.check_connection() == False or CLOUD_CONFIG == None:
        gwlogging.sendLog(gwlogging.ERR, "GW must be configured before Web Server can be disabled", MOD)
        pass
    elif GW_CONFIG == None:
        temp = {}
        temp['web'] = 0
        config_manager.write_gw(temp)
        sleep(5)
        reset()
    elif GW_CONFIG['web'] == 1:
        temp = GW_CONFIG
        temp['web'] = 0
        config_manager.write_gw(temp)
        sleep(5)
        reset()
    else:
        temp = GW_CONFIG
        temp['web'] = 1
        config_manager.write_gw(temp)
        sleep(5)
        reset()

async def long_press():
    gwlogging.sendLog(gwlogging.INFO, "Long Press Detected", MOD)
    fast_pulse(5)
    await asyncio.sleep_ms(2000)
    import os
    try:
        os.remove('wifi.json')
    except:
        #catches if file doesn't exist
        reset()
    await asyncio.sleep_ms(2000)
    reset()


async def killer():
    while resetVal == None:
        await asyncio.sleep_ms(50)

def run():
    try:
        asyncio.run(killer())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()

# Test for the Pushbutton class (coroutines)
# Pass True to test suppress
def test_btn(suppress=False, lf=True, df=True):
    pin = Pin(2, Pin.IN, Pin.PULL_UP)
    pb = Pushbutton(pin, suppress)
    if df:
        print('Doubleclick enabled')
        pb.double_func(double_press, ())
    if lf:
        print('Long press enabled')
        pb.long_func(long_press, ())
    run()

# Test for the Pushbutton class (callbacks)
def test_btncb():
    pin = Pin(2, Pin.IN, Pin.PULL_UP)
    pb = Pushbutton(pin)
    pb.double_func(double_press, ())
    pb.long_func(long_press, ())
    run()

_thread.start_new_thread(test_btn, ())

MOD = "MAIN"

def restart():
    sleep(10)
    reset()

wlan = wifimgr.get_connection()
if wlan is None:
    while True:
        sleep(1)

def time_stamp(time):
  return "{}-{:0>2d}-{:0>2d}{}{:0>2d}:{:0>2d}:{:0>2d}{}".format(time[0], time[1], time[2], "T", time[3], time[4], time[5], "Z")

if wifimgr.check_connection():
    sleep(5)
    settime()


# ============================================================================
# ============================================================================
# ============================================================================

if GW_CONFIG == None or GW_CONFIG['web'] == 1:
    @WebRoute(GET, '/wifi', name='WiFi')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        if wifimgr.check_connection():
            content = head1 + wifi_selected + head2 + """

                            <div class="header">

                                <h1> WiFi Already Configured</h1>
                            </div>
                            """ + end
            request.Response.ReturnOk(content)

        else:
            ssids = wifimgr.do_scan()

            content = head_small + wifi1
            while len(ssids):
                    ssid = ssids.pop(0)
                    content = content + """<label for="ssid" class="pure-radio"> <input type="radio" name="ssid" value="{0}">{0} </label>""".format(ssid)
            content = content +  wifi2 + end
            request.Response.ReturnOk(content)



    # ------------------------------------------------------------------------
    @WebRoute(POST, '/wifi-rescan', name='WiFi Rescan')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        ssids = wifimgr.do_scan()

        content = head_small + wifi1
        while len(ssids):
                ssid = ssids.pop(0)
                content = content + """<label for="ssid" class="pure-radio"> <input type="radio" name="ssid" value="{0}">{0} </label>""".format(ssid)
        content = content +  wifi2 + end
        request.Response.ReturnOk(content)
        if resetVal:
            import _thread
            _thread.start_new_thread(restart, ())



    # ------------------------------------------------------------------------

    @WebRoute(POST, '/wifi-post', name='wifi-post')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        try :
            if wifimgr.write_wifi(data):
                print("WiFi Config Saved")
            if wifimgr.do_connect(data):
                print("WiFi Connected")
        except :
            request.Response.ReturnBadRequest()
            return
        content = head1 + wifi_selected + head2 + """
                            <div class="header">
                                <h1> WiFi Configured</h1>
                            </div>
                            """ + end
        request.Response.ReturnOk(content)
        if wifimgr.check_connection():
            sleep(2)
            settime()
            gwlogging.sendLog(gwlogging.INFO, "Time Set", MOD)

    # ------------------------------------------------------------------------
    @WebRoute(GET, '/syslog', name='Syslog')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        if config_manager.check_sys() == True:
            content = head1 + sys_selected + head2 + """
                                <div class="header">
                                    <h1> Syslog Already Configured</h1>
                                </div>
                                """ + end
            request.Response.ReturnOk(content)

        else:
            content = head_small + sys_mode + end
            request.Response.ReturnOk(content)

    # ------------------------------------------------------------------------
    @WebRoute(POST, '/syslog-reconfigure', name='Syslog Reconfigure')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        content = head_small + sys_mode + end
        request.Response.ReturnOk(content)

    # ------------------------------------------------------------------------

    @WebRoute(POST, '/syslog-post', name='Syslog-post')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        try :
            config_manager.write_sys(data)
        except :
            request.Response.ReturnBadRequest()
            return
        content = head1 + sys_selected + head2 + """

                            <div class="header">

                                <h1> Syslog Configured</h1>

                            </div>
                            """ + end
        request.Response.ReturnOk(content)
        import _thread
        _thread.start_new_thread(restart, ())

    # ------------------------------------------------------------------------
    @WebRoute(GET, '/cloud', name='Cloud')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        if not wifimgr.check_connection():
            content = head1 + cloud_selected + head2 + """
                            <div class="header">
                                <h1>WiFi Configuration Missing</h1>
                                <h2> WiFi is required before this is available</h2>
                            </div>
                            """ + end
            request.Response.ReturnOk(content)

        else:
            if CLOUD_CONFIG == None:
                content = head_small + cloud_mode + end
                request.Response.ReturnOk(content)
            else:
                content = head1 + cloud_selected + head2 + """
                                    <div class="header">
                                        <h1> Cloud Connection Already Configured</h1>
                                    </div>
                                    """ + end
                request.Response.ReturnOk(content)

    # ------------------------------------------------------------------------
    @WebRoute(POST, '/cloud-reconfigure', name='Cloud Reconfigure')
    def RequestTestPost(microWebSrv2, request) :
            gc.collect()
            content = head1 + none_selected + head2 + cloud_mode + end
            request.Response.ReturnOk(content)

    # ------------------------------------------------------------------------

    @WebRoute(POST, '/cloud-post', name='Cloud-post')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        try :
            if data['mode'] == '1':
                content = head_small + cloud_mqtt + end
            else:
                content = head_small + cloud_http + end
        except :
            request.Response.ReturnBadRequest()
            return
        request.Response.ReturnOk(content)

    # ------------------------------------------------------------------------

    @WebRoute(POST, '/cloud-postmqtt', name='Cloud-postmqtt')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        data['mode'] = 1
        try :
            config_manager.write_cloud(data)
        except :
            request.Response.ReturnBadRequest()
            return
        content = head1 + cloud_selected + head2 + """

                            <div class="header">

                                <h1> MQTT Configured</h1>

                            </div>
                            """ + end
        global CLOUD_CONFIG
        CLOUD_CONFIG = data
        request.Response.ReturnOk(content)
        if resetVal:
            try:
                #Thread allow web server to respond back
                import _thread
                _thread.start_new_thread(restart, ())
            except:
                reset()

    # ------------------------------------------------------------------------

    @WebRoute(POST, '/cloud-posthttp', name='Cloud-posthttp')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        data['mode'] = 0
        try :
            config_manager.write_cloud(data)
        except :
            request.Response.ReturnBadRequest()
            return
        content = head1 + cloud_selected + head2 + """

                            <div class="header">

                                <h1> HTTP Configured</h1>

                            </div>
                            """ + end
        global CLOUD_CONFIG
        CLOUD_CONFIG = data
        request.Response.ReturnOk(content)
        if resetVal:
            try:
                #Thread allow web server to respond back
                import _thread
                _thread.start_new_thread(restart, ())
            except:
                reset()

    # ------------------------------------------------------------------------
    @WebRoute(GET, '/restart', name='restart')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        content = head1+ restart_selected + head2 + restart_content + end
        request.Response.ReturnOk(content)

    # ------------------------------------------------------------------------

    @WebRoute(POST, '/restart-post', name='restartPost')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        try :
            if data['restart'] == '0':
                content = head1 + restart_selected + head2 + """

                                    <div class="header">

                                        <h1> Restart Cancelled</h1>

                                    </div>
                                    """ + end
                request.Response.ReturnOk(content)
            elif data['restart'] == '1':
                gwlogging.sendLog(gwlogging.DEBUG, "Restarting. Inititated via web.", MOD)
                content = head1 + restart_selected + head2 + """

                                    <div class="header">

                                        <h1> Ruuvi GW Restarting</h1>

                                    </div>
                                    """ + end
                request.Response.ReturnOk(content)
                import _thread
                _thread.start_new_thread(restart, ())
        except :
            request.Response.ReturnBadRequest()
            return


    # ------------------------------------------------------------------------

    @WebRoute(POST, '/reset-gw', name='ResetGW')
    def RequestTestPost(microWebSrv2, request) :
        gc.collect()
        data = request.GetPostedURLEncodedForm()
        try :
            if data['resetM'] == '0':
                gwlogging.sendLog(gwlogging.DEBUG, "Removing Wifi Configuration", MOD)
                gwlogging.sendLog(gwlogging.DEBUG, "Gateway will restart", MOD)
                import os
                os.remove('wifi.json')
                sleep(2)
                reset()
            elif data['resetM'] == '1':
                gwlogging.sendLog(gwlogging.DEBUG, "Performing WiFi scan", MOD)
                global resetVal
                resetVal = 1
                request.Response.ReturnRedirect('/wifi-rescan')
            elif data['resetM'] == '2':
                gwlogging.sendLog(gwlogging.DEBUG, "Resetting Cloud Configuration", MOD)
                global resetVal
                resetVal = 1
                request.Response.ReturnRedirect('/cloud-reconfigure')
            elif data['resetM'] == '3':
                gwlogging.sendLog(gwlogging.DEBUG, "Resetting Syslog Server", MOD)
                global resetVal
                resetVal = 1
                request.Response.ReturnRedirect('/syslog-reconfigure')
            elif data['resetM'] == '4':
                gwlogging.sendLog(gwlogging.DEBUG, "Performing Factory Reset", MOD)
                gwlogging.sendLog(gwlogging.DEBUG, "Gateway will restart", MOD)
                import os
                os.remove('wifi.json')
                os.remove('gw.json')
                os.remove('wifi.json')
                os.remove('cloud.json')
                sleep(2)
                reset()
        except :
            request.Response.ReturnBadRequest()
            return

    # ============================================================================
    # ============================================================================
    # ============================================================================

    # Loads the PyhtmlTemplate module globally and configure it,
    pyhtmlMod = MicroWebSrv2.LoadModule('PyhtmlTemplate')
    pyhtmlMod.ShowDebug = True
    # Instanciates the MicroWebSrv2 class,
    mws2 = MicroWebSrv2()
    # For embedded MicroPython, use a very light configuration,
    mws2.SetEmbeddedConfig()
    # All pages not found will be redirected to the home '/',
    mws2.NotFoundURL = '/'
    # Starts the server as easily as possible in managed mode,
    mws2.StartManaged()

    # Main program loop until keyboard interrupt,
    try :
        while mws2.IsRunning :
            try:
                if int(CLOUD_CONFIG['mode']) == 0:
                    import gwhttp
                    pyhtmlMod.SetGlobalVar('GwMode', 0)
                    gwhttp.start(CLOUD_CONFIG)
                elif int(CLOUD_CONFIG['mode']) == 1:
                    import gwmqtt
                    pyhtmlMod.SetGlobalVar('GwMode', 1)
                    gwmqtt.start(CLOUD_CONFIG)
                else:
                    sleep(1)
                    pass
            except:
                fast_pulse(1)
                sleep(1)
    except KeyboardInterrupt:
        gwlogging.sendLog(gwlogging.NOTICE, "Exited from KeyboardInterrupt", MOD)
    # End,
    mws2.Stop()
else:
     # Main program loop until keyboard interrupt,
    try :
        while True:
            try:
                if int(CLOUD_CONFIG['mode']) == 0:
                    import gwhttp
                    gwhttp.start(CLOUD_CONFIG)
                elif int(CLOUD_CONFIG['mode']) == 1:
                    import gwmqtt
                    gwmqtt.start(CLOUD_CONFIG)
                else:
                    sleep(1)
                    pass
            except:
                fast_pulse(1)
                sleep(1)
    except KeyboardInterrupt:
        gwlogging.sendLog(gwlogging.NOTICE, "Exited from KeyboardInterrupt", MOD)
