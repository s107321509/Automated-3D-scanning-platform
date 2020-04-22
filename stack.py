def photo_stack(stack_step, microsteps):
	from time import sleep
	import RPi.GPIO as GPIO
	import os
	
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
		for x in range(microsteps):
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
        		sleep(delay)
		#execute shooting script
		os.system('./shoot.sh')
		#calculate how many microsteps the stack moves in total,and the parameter is used to return to the origin of the stack
		count+=stack_step_count 
		sleep(1)
	
	#return to stack origin
	GPIO.output(DIR,CW)
	for x in range(count):
        	GPIO.output(STEP, GPIO.HIGH)
        	sleep(delay)
        	GPIO.output(STEP, GPIO.LOW)
        	sleep(delay)
		
	sleep(.5)
	GPIO.cleanup()


