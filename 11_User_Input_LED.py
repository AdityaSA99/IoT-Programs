import RPi.GPIO as GPIO
import time

# GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print("HI***************")
while 1:
	a = int(input("Enter your choice : "))
	if a==1:
		GPIO.output(17,1)
	elif a==2:
		GPIO.output(27,1)
	elif a==3:
		GPIO.output(22,1)
	elif a==4:
		GPIO.output(17,0)
	elif a==5:
		GPIO.output(27,0)
	elif a==6:
		GPIO.output(22,0)
	elif a==7:
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,1)
	elif a==8:
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,0)
	else:
		continue