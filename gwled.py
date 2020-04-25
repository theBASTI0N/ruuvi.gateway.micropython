from machine import Pin
from time import sleep_ms
import _thread

led=Pin(23,Pin.OUT)

def pulse(count, ms):
    for i in range(count):
        led.on()
        sleep_ms(ms)
        led.off()

def slow_pulse(count):
    _thread.start_new_thread(pulse, (count, 1000))

def fast_pulse(count):
    _thread.start_new_thread(pulse, (count, 100))
