import machine
import time
from buzzer import Buzzer
from led_onboard import blink_led
from morse_code_translator import MorseTranslator

interval_speed = 0.1

freq = 262 # middle C
volume = 10000 # max volume?
pin = 15
buzzer = Buzzer(pin, freq, volume)

translator = MorseTranslator(interval_speed, buzzer, blink_led)

while True:
  translator.morse_code_translator('sos')
  time.sleep(interval_speed * 8)
