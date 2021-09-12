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
        GPIO.setup(trig_2,GPIO.OUT) # Trigger
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
        if distance1&lt;5:
        print(&quot;Tank Is Full&quot;)
        elif distance1&gt;8 and distance1&lt;12:
        print(&quot;Tank Is Approximately Half&quot;)
        elif distance1&gt;18 and distance1&lt;21:
        print(&quot;Tank Is Empty&quot;)
        z=x+&quot;,&quot;+y+&quot;\n&quot;
        print(z)
        file=&#39;text.txt&#39;
        with open(file,&#39;a&#39;) as filetowrite:
        filetowrite.write(z)
        filetowrite.close()
    GPIO.cleanup()
    return distance1
while True:
    ping()