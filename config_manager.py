import json
import uos

GW_CONF_FILE = 'gw.json'
SYSLOG_CONF_FILE = 'syslog.json'
CLOUD_CONF_FILE = 'cloud.json'

def read_gw():
    with open(GW_CONF_FILE) as f:
        profiles = json.load(f)
    return profiles

def write_gw(profiles):
    with open(GW_CONF_FILE, 'w') as f:
        json.dump(profiles, f)
    return True

def check_gw():
    try:
        uos.stat(GW_CONF_FILE)
        return True
    except OSError:
        return False

def read_sys():
    with open(SYSLOG_CONF_FILE) as f:
        profiles = json.load(f)
    return profiles

def write_sys(profiles):
    with open(SYSLOG_CONF_FILE, 'w') as f:
        json.dump(profiles, f)
    return True

def check_sys():
    try:
        uos.stat(SYSLOG_CONF_FILE)
        return True
    except OSError:
        return False

def read_cloud():
    with open(CLOUD_CONF_FILE) as f:
        profiles = json.load(f)
    return profiles

def write_cloud(profiles):
    with open(CLOUD_CONF_FILE, 'w') as f:
        json.dump(profiles, f)
    return True

def check_cloud():
    try:
        uos.stat(CLOUD_CONF_FILE)
        return True
    except OSError:
        return False
