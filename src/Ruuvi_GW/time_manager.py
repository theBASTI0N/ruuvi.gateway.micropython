from time import localtime, sleep, time

# Return Human Redable Time Stamp
# Eg.
def time_stamp():
    now = localtime()
    return "{}-{:0>2d}-{:0>2d}{}{:0>2d}:{:0>2d}:{:0>2d}{}".format(now[0], now[1], now[2], "T", now[3], now[4], now[5], "Z")

# Returns Epoch/Unix Time stamp. 
# Eg. 1609304885
# GMT: Wednesday, December 30, 2020 5:08:05 AM
def unix_time_stamp():
    return time() + 946684800