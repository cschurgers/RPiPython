#not 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)

state = True

for i in range(0,4):
    GPIO.output(7,state)
    print 'led in state ' + str(state)
    state = not state
    time.sleep(1)

GPIO.cleanup()
