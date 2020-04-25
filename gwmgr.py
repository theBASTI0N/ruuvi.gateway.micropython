import json
import uos

GW_PROFILES = 'gw.json'
SYSLOG_PROFILE = 'syslog.json'

def read_gw():
    with open(GW_PROFILES) as f:
        profiles = json.load(f)
    return profiles

def write_gw(profiles):
    with open(GW_PROFILES, 'w') as f:
        json.dump(profiles, f)
    return True

def read_sys():
    with open(SYSLOG_PROFILE) as f:
        profiles = json.load(f)
    return profiles

def write_sys(profiles):
    with open(SYSLOG_PROFILE, 'w') as f:
        json.dump(profiles, f)
    return True

def check_sys():
    try:
        uos.stat(SYSLOG_PROFILE)
        return True
    except OSError:
        return False
