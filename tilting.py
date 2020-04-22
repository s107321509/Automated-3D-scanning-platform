def tilt(stack_step, microsteps):
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
	
	delay = 0.0001
	sum=0
	
	#how many images are needed for each horizontal turn?
	panning_step=[40, 40, 40]
	#define any number of tilt angles,each 100 microsteps is about 4.5 degrees
	tilting_step=[300, 300, 300]
	
	#the tilt axis moves to the tilt angle defined by tilting_step
	GPIO.output(DIR,CCW)
	for x in range(len(tilting_step)):
		for y in range(tilting_step[x]):
			GPIO.output(STEP,GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
			sleep(delay)
		#accumulate microsteps of each tilting move,the parameters is used to return the origin of the tilt axis
		sum+=tilting_step[x]
		sleep(2)
		
 		panning.panning_rotation(panning_step[x], stack_step, microsteps)
  		sleep(1)
		
  		DIR = 20
  		STEP = 21
  		GPIO.setmode(GPIO.BCM)
  		GPIO.setup(DIR, GPIO.OUT)
  		GPIO.setup(STEP, GPIO.OUT)
		
	#back to tilting origin	
	GPIO.output(DIR, CW)
	for x in range(sum):
  		GPIO.output(STEP,GPIO.HIGH)
  		sleep(delay)
  		GPIO.output(STEP, GPIO.LOW)
  		sleep(delay)

	sleep(.5)
	GPIO.cleanup()

