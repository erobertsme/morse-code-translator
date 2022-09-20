import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

def blink_led(interval_speed, n):
  led.on()
  time.sleep(n)
  led.off()
  time.sleep(interval_speed)
