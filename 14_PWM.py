import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
p=GPIO.PWM(17,1000)
p.start(50)
print("hello..!!pwm start with 50% brightness")
sleep(1)
while 1:
	#p = changeDutyCycle(50)
	print("pwm is inside loop")
	sleep(2)
	p.ChangeDutyCycle(90)
	print("brightness is 90%")
	sleep(2)
	p.ChangeDutyCycle(60)
	print("brightness is 60%")
	sleep(2)
	p.ChangeDutyCycle(30)
	print("brightness is 30%")
	sleep(2)
	p.ChangeDutyCycle(0)
	print("brightness is 0%")
	sleep(2)




