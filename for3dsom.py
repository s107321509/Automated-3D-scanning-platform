def turn(stack_step, step_cnt):
	from time import sleep
	import RPi.GPIO as GPIO
	import os
	import cir

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
	horizontal_step=[10, 10, 10]
	step_count=[300, 300, 350]
	for x in range(3):
		for y in range(step_count[x]):
			GPIO.output(STEP,GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
			sleep(delay)
		sum+=step_count[x]
		sleep(2)
 		cir.horizontal_rotation(horizontal_step[x], stack_step, step_cnt)
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

