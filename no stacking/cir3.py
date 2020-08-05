def horizontal_rotation(revnum):
  from time import sleep
  import RPi.GPIO as GPIO
  import os

  DIR =18 
  STEP =14
  CW = 1
  CCW = 0
  SPR = 1600/revnum

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DIR, GPIO.OUT)
  GPIO.setup(STEP, GPIO.OUT)
  GPIO.output(DIR, CW)

  step_count = SPR
  delay = .005


  for x in range(revnum):
    for y in range(step_count):
      GPIO.output(STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(STEP, GPIO.LOW)
      sleep(delay)
    os.system('./run.sh')
    sleep(2)

  sleep(.5)
  GPIO.cleanup()
