import usyslog
from gwmgr import read_sys, read_gw

# Alert Level
EMERG = const(0)
ALERT = const(1)
CRIT = const(2)
ERR = const(3)
WARN = const(4)
NOTICE = const(5)
INFO = const(6)
DEBUG = const(7)

TYPE_STR = {
    DEBUG   : 'DEBUG',
    INFO    : 'INFO',
    WARN : 'WARNING',
    ERR   : 'ERROR',
    NOTICE    : 'NOTICE',
    CRIT: 'CRITICAL',
    ALERT: 'ALERT',
    EMERG : 'EMERG'
}

try:
    sysCONF = read_sys()
except:
    print("Could not get SYSLOG configuration")
    try:
        sysCONF = read_gw()
        sysCONF['TZ'] = 0
        sysCONF['syslog'] = 0
        sysCONF['port'] = 514
    except:
        sysCONF = { 'host': '0.0.0.0', 'TZ': 0, 'syslog': 0, 'port': 514}
        print("SYSLOG unable to be configured")

def sendLog(level, message, mod):
    t = TYPE_STR[level]
    print("[SYSLOG %s] " % t + mod + ": " + message)
    if int(sysCONF['syslog']) == 0:
        u = usyslog.UDPClient(ip=sysCONF['host'], port=sysCONF['port'])
        if level==ALERT:
            u.alert(message, mod, sysCONF['TZ'])
        elif level==CRIT:
            u.critical(message, mod, sysCONF['TZ'])
        elif level==ERR:
            u.error(message, mod, sysCONF['TZ'])
        elif level==WARN:
            u.warning(message, mod, sysCONF['TZ'])
        elif level==NOTICE:
            u.notice(message, mod, sysCONF['TZ'])
        elif level==INFO:
            u.info(message, mod, sysCONF['TZ'])
        elif level==DEBUG:
            u.debug(message, mod, sysCONF['TZ'])
        else:
            u.log(usyslog.S_EMERG, message, mod, sysCONF['TZ'])
        u.close()
    elif int(sysCONF['syslog']) == 1:
        u = usyslog.TCPClient(ip=sysCONF['host'], port=sysCONF['port'])
        if level==ALERT:
            u.alert(message, mod, sysCONF['TZ'])
        elif level==CRIT:
            u.critical(message, mod, sysCONF['TZ'])
        elif level==ERR:
            u.error(message, mod, sysCONF['TZ'])
        elif level==WARN:
            u.warning(message, mod, sysCONF['TZ'])
        elif level==NOTICE:
            u.notice(message, mod, sysCONF['TZ'])
        elif level==INFO:
            u.info(message, mod, sysCONF['TZ'])
        elif level==DEBUG:
            u.debug(message, mod, sysCONF['TZ'])
        else:
            u.log(usyslog.S_EMERG, message, mod, sysCONF['TZ'])
        u.close()
