def panning_rotation(panning_step, stack_step, microsteps):
  from time import sleep
  import RPi.GPIO as GPIO
  import os
  import stack

  DIR =18 
  STEP =14
  CW = 1
  CCW = 0
  SPR = 1600/panning_step

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DIR, GPIO.OUT)
  GPIO.setup(STEP, GPIO.OUT)
  
  delay = .005
  step_count=SPR
  
  GPIO.output(DIR, CW)
  for x in range(panning_step):
    for y in range(step_count):
      GPIO.output(STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(STEP, GPIO.LOW)
      sleep(delay)
    sleep(2)
    #when each turntable rotates, execute the stack function
    stack.photo_stack(stack_step, microsteps)
    sleep(1)
    
    DIR =18 
    STEP =14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)

  sleep(.5)
  GPIO.cleanup()

