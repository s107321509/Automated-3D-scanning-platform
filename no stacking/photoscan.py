from time import sleep
import RPi.GPIO as GPIO
import os
import cir3
import time
st = time.time()
DIR = 20
STEP = 21
CW = 1
CCW = 0
#SPR = 400 

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR,CCW)

#step_count = SPR
delay = 0.0001
# callCir3 = 'python cir3.py'
# callCir4 = 'python cir4.py'

#count=0
sum=0
horizontal_step=[40, 40, 40]
step_count=[300, 300, 300]
for x in range(3):
  for y in range(step_count[x]):
	GPIO.output(STEP,GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)
  #count = count + 1
  sum+=step_count[x]
  sleep(2)
  cir3.horizontal_rotation(horizontal_step[x])
  sleep(1)
  DIR = 20
  STEP = 21
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DIR, GPIO.OUT)
  GPIO.setup(STEP, GPIO.OUT)

#   if count<3:
#   	os.system(callCir3)
#   	sleep(1)
#   else:
#   	os.system(callCir4)
#   	sleep(1)

GPIO.output(DIR, CW)
for x in range(sum):
        GPIO.output(STEP,GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

sleep(.5)

end = time.time()
print(end - st)

