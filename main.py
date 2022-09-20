import machine
import time

interval_speed = 0.1

led = machine.Pin('LED', machine.Pin.OUT) # onboard LED

sound = True # this uses a simple buzzer
buzzer = machine.PWM(machine.Pin(15))
buzzer.freq(262) # middle C
volume = 10000 # max volume?

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
  ' ': '0'
}

def blink(n):
  led.on()
  time.sleep(n)
  led.off()
  time.sleep(interval_speed)

def beep(n):
  buzzer.duty_u16(volume)
  time.sleep(n)
  buzzer.duty_u16(0)

def translate_char(char):
  return map(lambda str: int(str), morse_code_translations[char])

def morse_code(morse_char_str):
  morse_char_integers = map(lambda str: int(str), morse_code_translations[morse_char_str])
  for n in morse_char_integers:
    interval = n * interval_speed
    if (n == 0):
      time.sleep(interval * 4)
      return
    
    if (sound == True):
      beep(interval)

    blink(interval)

def morse_code_translator(text):
  for char in text:
    morse_code(char.upper())
    time.sleep(interval_speed)

while (True):
  morse_code_translator('sos')
  time.sleep(interval_speed * 8)
