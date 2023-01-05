import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_RED=17
LED_BLUE=27
LED_GREEN=22
RGB=[LED_RED,LED_BLUE,LED_GREEN]

while 1:
    GPIO.setup(RGB, GPIO.OUT,initial=GPIO.LOW)
    for i in RGB:
        GPIO.output(i,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(i,GPIO.LOW)
        time.sleep(1)
    
        
  