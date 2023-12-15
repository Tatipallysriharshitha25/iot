import RPi.GPIO as A
import time
A.setwarnings(False)
A.setmode(A.BOARD)
A.setup(18,A.OUT)
A.setup(32,A.IN,pull_up_down=A.PUD_UP)
while (True):
    input_state=A.input(32)
    if(input_state==1):
        A.output(18,1)
        print('LED OFF')
    else:
        A.output(18,0)
        print('LED ON')