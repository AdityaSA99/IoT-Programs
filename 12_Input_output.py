import RPi.GPIO as GPIO
import time

# GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
while 1:
	a = GPIO.input(24)
	if(a==1):
		GPIO.output(17,1)
		print("ON----------------")
	else:
		GPIO.output(17,0)
		print("OFF---------------")
	time.sleep(2)