import machine
import time
from machine import Timer

PIN_D5 = 14

class Root:
	def blink(self):
		pin = machine.Pin(PIN_D5, machine.Pin.OUT, machine.Pin.PULL_UP)
		tim = Timer(-1)
		pin.low()
		tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:pin.high())
	def blinking(self):
		pin = machine.Pin(PIN_D5, machine.Pin.OUT, machine.Pin.PULL_UP)
		tim = Timer(-1)
		tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:pin.value(not pin.value()))

if __name__ == '__main__':
    import sys
    print("root imported")