import RPi.GPIO as A
import time
A.setwarnings(False)
A.setmode(A.BCM)
A.setup(18,A.OUT)
A.setup(15,A.OUT)
A.setup(14,A.OUT)

print('LED ON')
while (True):
    A.output(18,0)
    A.output(14,1)
    A.output(15,1)
    time.sleep(1)
    A.output(18,1)
    A.output(14,0)
    A.output(15,1)
    time.sleep(1)
    A.output(18,1)
    A.output(14,1)
    A.output(15,0)
    time.sleep(1)
   


