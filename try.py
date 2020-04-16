from time import sleep
import RPi.GPIO as GPIO
import os
import for3dsom
#CW = forward ,CCW = backward
#1250 = 5mm
DIR=5
STEP=6
CW=0
CCW=1
SPR=500

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

step_count=SPR
delay=0.0001

class _Getch:
        def __init__(self):
                try:
                   self.impl = _GetchWindows()
                except ImportError:
                   self.impl = _GetchUnix()
        def __call__(self): return self.impl()

class _GetchUnix:
        def __init__(self):
                import tty, sys
        def __call__(self):
                import sys, tty, termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                   tty.setraw(sys.stdin.fileno())
                   ch = sys.stdin.read(1)
                finally:
                   termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
                return ch

class _GetchWindows:
        def __init__(self):
                import msvcrt
        def __call__(self):
                import msvcrt
                return msvcrt.getch()

getch = _Getch()
count = 0
#doing back or forward
print("Press 'w' to forward and press 's' to backward \n")
print("Press 'a'to set the point begin press 'd' to set the point end\n")
print("Press 'q' to finish\n")
while 1:
        a = getch()
        if(a == "w"):
                GPIO.output(DIR,CCW)

                for x in range(step_count):
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)


                count = count + 500
        if(a == "s"):
                GPIO.output(DIR,CW)

                for x in range(step_count):
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)

                count = count - 500
        if(a == "a"):
                begin = count
        if(a == "d"):
                end = count
#setting begin and end
        if(a == "q"):
                break
#back to begin
if(end > begin):
        GPIO.output(DIR,CW)
        for x in range(end-begin):
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)

print("\n\ndistance: {}mm".format((end-begin)/250))
#how many steps from begin to end
step = input("\nstep: ")

forward = (end-begin)/step
#GPIO.output(DIR,CCW)
#for i in range(step):
        #forward = (end - begin)/step
        #for x in range(forward):
                #GPIO.output(STEP, GPIO.HIGH)
                #sleep(delay)
                #GPIO.output(STEP, GPIO.LOW)
                #sleep(delay)
	#sleep(3)
        #os.system('./run.sh')
#sleep(1)
#back to origin
#GPIO.output(DIR,CW)
#for x in range(end-begin):
        #GPIO.output(STEP, GPIO.HIGH)
        #sleep(delay)
        #GPIO.output(STEP, GPIO.LOW)
        #sleep(delay)

#print("stack step count: {}".format(forward))
#print("total stack distance: {}mm".format((end-begin)/250))
#print("begin: {}mm".format(begin/250))
#print("end: {}mm".format(end/250))
GPIO.cleanup()
#cmd = 'python turn3dsom.py'
for3dsom.turn(step, forward)
