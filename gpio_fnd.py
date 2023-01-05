import RPi.GPIO as GPIO
import time


# GPIO output raspberry pi pinnum 
#        A   B   C   D   E   F   G   DP
seg = [16, 12, 26, 6, 5, 20, 21, 19]

num = 0


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


def FND_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(seg,GPIO.OUT,initial=GPIO.HIGH)

def main():
    i=0
    FND_setup()
    
    while True:
        for i in range (10) :
            GPIO.output(seg, fnd[i])
            time.sleep(1)
        
if __name__ == '__main__':
    main()