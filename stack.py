def photo_stack(stack_step, step_cnt):
	from time import sleep
	import RPi.GPIO as GPIO
	import os
	
#CW = forward ,CCW = backward
#1250 = 0.5cm
	DIR=5
	STEP=6
	CW=0
	CCW=1

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(DIR, GPIO.OUT)
	GPIO.setup(STEP, GPIO.OUT)
	delay=0.0001
	
	count=0
	GPIO.output(DIR, CCW)
	for i in range(stack_step):
		for x in range(step_cnt):
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
        		sleep(delay)
		#os.system('./run.sh')
		count+=step_cnt 
		sleep(1)
	GPIO.output(DIR,CW)
	for x in range(count):
        	GPIO.output(STEP, GPIO.HIGH)
        	sleep(delay)
        	GPIO.output(STEP, GPIO.LOW)
        	sleep(delay)
	sleep(.5)
	GPIO.cleanup()


