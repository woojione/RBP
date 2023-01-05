import RPi.GPIO as GPIO
import time
import I2C_driver
from time import *

# GPIO output raspberry pi pinnum 
#        A   B   C   D   E   F   G   DP
seg = [16, 12, 26, 6, 5, 20, 21, 19]


#seg=[  A B C D E F G DP ]
fnd = [(0,0,0,0,0,0,1,1),
    (1,0,0,1,1,1,1,1),
    (0,0,1,0,0,1,0,1),
    (0,0,0,0,1,1,0,1),#3
    (1,0,0,1,1,0,0,1),
    (0,1,0,0,1,0,0,1),
    (0,1,0,0,0,0,0,1),#6
    (0,0,0,1,1,0,1,1),
    (0,0,0,0,0,0,0,1),
    (0,0,0,0,1,0,0,1)]

# mylcd = RPi_I2C_driver.lcd()
mylcd = I2C_driver.lcd()
# test 2
mylcd.lcd_display_string("RPi I2C test", 1)
mylcd.lcd_display_string(" Custom chars", 2)

sleep(2) # 2 sec delay

mylcd.lcd_clear()

# let's define a custom icon, consisting of 6 individual characters
# 3 chars in the first row and 3 chars in the second row
fontdata1 = [
        # Char 0 - Upper-left
        [ 0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10 ],
        # Char 1 - Upper-middle
        [ 0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00 ],
        # Char 2 - Upper-right
        [ 0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01 ],
        # Char 3 - Lower-left
        [ 0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00 ],
        # Char 4 - Lower-middle
        [ 0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00 ],
        # Char 5 - Lower-right
        [ 0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00 ],
        # Char 6 - my test
	[ 0x1f,0x0,0x4,0xe,0x0,0x1f,0x1f,0x1f],
]

# Now let's define some more custom characters
fontdata2 = [
        # Char 0 - left arrow
        [ 0x1,0x3,0x7,0xf,0xf,0x7,0x3,0x1 ],
        # Char 1 - left one bar 
        [ 0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10 ],
        # Char 2 - left two bars
        [ 0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18 ],
        # Char 3 - left 3 bars
        [ 0x1c,0x1c,0x1c,0x1c,0x1c,0x1c,0x1c,0x1c ],
        # Char 4 - left 4 bars
        [ 0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e ],
        # Char 5 - left start
        [ 0x0,0x1,0x3,0x7,0xf,0x1f,0x1f,0x1f ],
        # Char 6 - 
        # [ ],
]


def FND_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(seg,GPIO.OUT,initial=GPIO.HIGH)

def main():
    i=0
    FND_setup()
    MaxDuty= 12 
    print('Wating for 1 sec') 
    sleep(1) 
    
    PWMpin= 18 #BOARD 12
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(PWMpin, GPIO.OUT) 
    Servo=GPIO.PWM(PWMpin, 50) 
    
    Servo.start(0)
    
    while True:
        C=int(input('Enter key: '))
        duty_ratio=int(input('duty_Ratdio: ')) # Duty %
        if C>=0&C<10:
            GPIO.output(seg, fnd[C])
            sleep(1)
            mylcd.lcd_display_string_pos("Your Choice: ",1,1)
            mylcd.lcd_display_string_pos(str(C),1,14)# row 2, column 3
            if duty_ratio <= MaxDuty:
                Servo.ChangeDutyCycle(duty_ratio)
                sleep(2)
                duty_ratio+= 1
            elif duty_ratio == MaxDuty:
                duty_ratio= 0
                Servo.ChangeDutyCycle(duty_ratio)
            Servo.stop()
        GPIO.cleanup()
        print('Everythings cleanup')
        sleep(1)
            
        mylcd.lcd_clear()
        
if __name__ == '__main__':
    main()