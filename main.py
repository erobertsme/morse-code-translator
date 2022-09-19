import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

interval_speed = 0.2

morse_code_translations = {
  'A': '12',
  'B': '2111',
  'C': '2121',
  'D': '211',
  'E': '1',
  'F': '1121',
  'G': '221',
  'H': '1111',
  'I': '11',
  'J': '1222',
  'K': '212',
  'L': '1211',
  'M': '22',
  'N': '21',
  'O': '222',
  'P': '1221',
  'Q': '2212',
  'R': '121',
  'S': '111',
  'T': '2',
  'U': '112',
  'V': '1112',
  'W': '122',
  'X': '2112',
  'Y': '2122',
  'Z': '2211',
}

def blink(n):
  led.on()
  time.sleep(n)
  led.off()
  time.sleep(interval_speed)

def blink_char(char_intervals):
  for interval in char_intervals:
    blink(interval * interval_speed)

def translate_char(char):
  return map(lambda str: int(str), morse_code_translations[char])

def morse_code(translation):
  for char in translation:
    blink_char(translate_char(char))

def morse_code_translator(text):
  for char in text:
    morse_code(char.upper())
    time.sleep(interval_speed)

while (True):
  morse_code_translator('fuck')
  time.sleep(interval_speed * 4)
