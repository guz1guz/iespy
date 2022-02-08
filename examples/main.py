"""Your main code goes here!"""

import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

while True:
  led.value(1)
 
