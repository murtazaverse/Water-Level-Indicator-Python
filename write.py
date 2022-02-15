import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import RPi.GPIO as GPIO
def ping():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    trig_2 = 26
    echo_2 = 19
    while True:
     # Echo
        GPIO.setup(trig_2,GPIO.OUT)  # Trigger
        GPIO.setup(echo_2,GPIO.IN)
        GPIO.output(trig_2, False)
        time.sleep(1.5)
        GPIO.output(trig_2, True)
        time.sleep(0.001)
        GPIO.output(trig_2, False)
        start1 = time.time()
        while GPIO.input(echo_2)==0:
            start1 = time.time()
        while GPIO.input(echo_2)==1:
            stop1= time.time()
        elapsed1 = stop1-start1
        distancet1 = (elapsed1*34300)-0.5
        distance1 = distancet1/2
        elapsed1=round(elapsed1,6)
    
        distance1 = round(distance1,0)
        y=str(distance1)
        x=str(elapsed1)
        if distance1<5:
            print("Tank Is Full")
        elif distance1>8 and distance1<12:
            print("Tank Is Approximately Half")
        elif distance1>18 and distance1<21:
            print("Tank Is Empty")
        z=x+","+y+"\n"
        print(z)
        file='text.txt'
        with open(file,'a') as filetowrite:
            filetowrite.write(z)
            filetowrite.close()
    GPIO.cleanup()
    return distance1
while True:
    ping()
