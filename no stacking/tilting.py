#how many images are needed for each horizontal turn?
panning_step=[40, 40, 40]
#define any number of tilt angles,each 100 microsteps is about 4.5 degrees
tilting_step=[300, 300, 300]

from time import sleep
import RPi.GPIO as GPIO
import os
import panning
import time
st = time.time()
DIR = 20
STEP = 21
CW = 1
CCW = 0

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR,CCW)


delay = 0.0001

sum=0
for x in range(len(tilting_step)):
  for y in range(tilting_step[x]):
    GPIO.output(STEP,GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
  
  #Tilt step accumulation
  sum+=tilting_step[x]
  sleep(2)
  
  #Pass the parameters into the panning.py
  panning.horizontal_rotation(panning_step[x])
  sleep(1)
  DIR = 20
  STEP = 21
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DIR, GPIO.OUT)
  GPIO.setup(STEP, GPIO.OUT)

#Return to tilting origin
GPIO.output(DIR, CW)
for x in range(sum):
        GPIO.output(STEP,GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

sleep(.5)

end = time.time()
print(end - st)

