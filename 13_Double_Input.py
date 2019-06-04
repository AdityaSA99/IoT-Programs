import RPi.GPIO as GPIO
import time

count=0
# GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
while 1:
	a = GPIO.input(23)
	b = GPIO.input(24)

	if(a==0 and b==0 and count==0):
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,0)
		print("000----------------")
		count = 1
	elif(a==0 and b==0 and count==1):
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,1)
		print("111---------------")
		count = 0
	if(a==0 and b==1 and count==0):
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,1)
		print("001----------------")
		count = 1
	elif(a==0 and b==1 and count==1):
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,0)
		print("110---------------")
		count = 0
	if(a==1 and b==0 and count==0):
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,0)
		print("010----------------")
		count = 1
	elif(a==1 and b==0 and count==1):
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,1)
		print("101---------------")
		count = 0
	if(a==1 and b==1 and count==0):
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,0)
		print("100----------------")
		count = 1
	elif(a==1 and b==1 and count==1):
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,1)
		print("011---------------")
		count = 0
	time.sleep(2)
