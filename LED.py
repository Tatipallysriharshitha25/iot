import RPi.GPIO as A
import time
A.setwarnings(False)
A.setmode(A.BCM)
A.setup(18,A.OUT)
A.output(18,0)
print('LED ON')
time.sleep(1)