import RPi.GPIO as A
import time
A.setwarnings(False)
A.setmode(A.BCM)
TRIG=21
ECHO=20
A.setup(TRIG,A.OUT)
A.setup(ECHO,A.IN)
while True:
    A.output(TRIG,False)
    time.sleep(2)
    A.output(TRIG,True)
    time.sleep(0.0001)
    A.output(TRIG,False)
    while A.input(ECHO)==0:
        pulse_start=time.time()
    while A.input(ECHO)==1:    
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,0)
    if distance>2 and distance<100:
        print("Distance:",distance,"cm")
    else:
        print("out of range")