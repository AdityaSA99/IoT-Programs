import RPi.GPIO as GPIO
import time

# GPIO Setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print("HI***************")
while 1:
	for i in range(0,11):
		print("LED ON -----------------------------              :)		")
		GPIO.output(17,1)
		time.sleep(i/5)
		GPIO.output(17,0)
		GPIO.output(27,1)
		time.sleep(i/5)
		GPIO.output(27,0)
		GPIO.output(22,1)
		time.sleep(i/5)
		GPIO.output(22,0)
		time.sleep(i/5)
		print("LED OFF -----------------------------                :(		")
