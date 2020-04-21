def tilting(stack_step, step_cnt):
	from time import sleep
	import RPi.GPIO as GPIO
	import os
	import panning

	DIR = 20
	STEP = 21
	CW = 1
	CCW = 0
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(DIR, GPIO.OUT)
	GPIO.setup(STEP, GPIO.OUT)
	GPIO.output(DIR,CCW)

	delay = 0.0001
	sum=0
	
	panning_step=[40, 40, 40]
	tilting_step=[300, 300, 300]
	
	for x in range(3):
		for y in range(tilting_step[x]):
			GPIO.output(STEP,GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
			sleep(delay)
		sum+=tilting_step[x]
		sleep(2)
		
 		panning.panning_rotation(panning_step[x], stack_step, step_cnt)
  		sleep(1)
  		DIR = 20
  		STEP = 21
  		GPIO.setmode(GPIO.BCM)
  		GPIO.setup(DIR, GPIO.OUT)
  		GPIO.setup(STEP, GPIO.OUT)
	GPIO.output(DIR, CW)
	for x in range(sum):
  		GPIO.output(STEP,GPIO.HIGH)
  		sleep(delay)
  		GPIO.output(STEP, GPIO.LOW)
  		sleep(delay)

	sleep(.5)
	GPIO.cleanup()

