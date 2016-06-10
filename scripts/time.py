#http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html

import machine
import time
pin_d5 = 14
pin = machine.Pin(pin_d5, machine.Pin.OUT, machine.Pin.PULL_UP)
pin.high()

while True:
	pin.high()
	time.sleep(1)
	pin.low()
	time.sleep(1)

machine.PWM(machine.Pin(pin_d5), freq=1000, duty=50)

