import time

class MorseTranslator:
  def __init__(self, interval_speed, sound, led):
    self.interval_speed = interval_speed

    if sound != False:
      self.sound_on = True
      self.buzzer = sound

    if led != False:
      self.led_on = True
      self.blink_led = led

    self.translations = {
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

  def run_morse_code(self, morse_char_integers):
    for n in morse_char_integers:
      interval = n * self.interval_speed

      if n == 0:
        time.sleep(interval * 4)
        return

      if self.sound_on == True:
        self.buzzer.beep(interval)

      if self.led_on == True:
        self.blink_led(self.interval_speed, interval)

  def morse_code_translator(self, text):
    for char in text:
      morse_char_integers = map(lambda str: int(str), self.translations[char.upper()])
      self.run_morse_code(morse_char_integers)
      time.sleep(self.interval_speed)
