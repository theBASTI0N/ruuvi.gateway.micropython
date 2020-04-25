"""
Based on https://github.com/kfricke/micropython-usyslog
"""
import usocket
from requests import id
from time import localtime, time

MONTHS = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def time_stamp(time):
  return "{} {} {:0>2d} {:0>2d}:{:0>2d}:{:0>2d}".format(time[0], MONTHS[time[1]], time[2], time[3], time[4], time[5])

# Facility constants
F_KERN = const(0)
F_USER = const(1)
F_MAIL = const(2)
F_DAEMON = const(3)
F_AUTH = const(4)
F_SYSLOG = const(5)
F_LPR = const(6)
F_NEWS = const(7)
F_UUCP = const(8)
F_CRON = const(9)
F_AUTHPRIV = const(10)
F_FTP = const(11)
F_NTP = const(12)
F_AUDIT = const(13)
F_ALERT = const(14)
F_CLOCK = const(15)
F_LOCAL0 = const(16)
F_LOCAL1 = const(17)
F_LOCAL2 = const(18)
F_LOCAL3 = const(19)
F_LOCAL4 = const(20)
F_LOCAL5 = const(21)
F_LOCAL6 = const(22)
F_LOCAL7 = const(23)

# Severity constants (Names reasonably shortened)
S_EMERG = const(0)
S_ALERT = const(1)
S_CRIT = const(2)
S_ERR = const(3)
S_WARN = const(4)
S_NOTICE = const(5)
S_INFO = const(6)
S_DEBUG = const(7)

class SyslogClient:
    def __init__(self, facility=F_SYSLOG):
        self._facility = facility

    def log(self, severity, msg, module, tz):
        pass

    def alert(self, msg, module, tz):
        self.log(S_ALERT, msg, module, tz)

    def critical(self, msg, module, tz):
        self.log(S_CRIT, msg, module, tz)

    def error(self, msg, module, tz):
        self.log(S_ERR, msg, module, tz)

    def debug(self, msg, module, tz):
        self.log(S_DEBUG, msg, module, tz)

    def info(self, msg, module, tz):
        self.log(S_INFO, msg, module, tz)

    def notice(self, msg, module, tz):
        self.log(S_NOTICE, msg, module, tz)

    def warning(self, msg, module, tz):
        self.log(S_WARN, msg, module, tz)

class UDPClient(SyslogClient):
    def __init__(self, ip='127.0.0.1', port=514, facility=F_SYSLOG):
        self._addr = usocket.getaddrinfo(ip, port)[0][4]
        self._sock = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
        super().__init__(facility)

    def log(self, severity, msg, module, tz):
        data = "<%d>%s %s RuuviGW[%s]: %s" % (severity + (self._facility << 3), time_stamp(localtime(time() + 946684800 + (int(tz) * 3600))), id, module, msg)
        self._sock.sendto(data.encode(), self._addr)

    def close(self):
        self._sock.close()

class TCPClient(SyslogClient):
    def __init__(self, ip='127.0.0.1', port=514, facility=F_SYSLOG):
        self._sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        self._sock.connect((ip, port))
        super().__init__(facility)

    def log(self, severity, msg, module, tz):
        data = "<%d>%s %s RuuviGW[%s]: %s" % (severity + (self._facility << 3), time_stamp(localtime(time() + 946684800 + (int(tz) * 3600))), id, module, msg)
        self._sock.send(data.encode())

    def close(self):
        self._sock.close()
