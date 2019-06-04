import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
p = GPIO.PWM(17,1000)
s =GPIO.PWM(27,1500)
r =GPIO.PWM(22,2000)
p.start(50)
s.start(70)
r.start(100)
print("hello..!!PWM started with 50% Rotation Speed")
print("hello..!!PWM started with 70% Rotation Speed")
print("hello..!!PWM started with 100% Rotation Speed")
sleep(1)
	while 1:
		p.ChangeDutyCyle(90)
		print("Rotation Speed 90%")
		sleep(2)
		p.ChangeDutyCyle(50)
		print("Rotation Speed 50%")
		sleep(2)
		p.ChangeDutyCyle(0)
		print("Rotation Speed 0%")
		sleep(2)
		r.ChangeDutyCyle(20)
		print("Rotation Speed 20%")
		sleep(2)
		r.ChangeDutyCyle(0)
		print("Rotation Speed 0%")
		sleep(2)
		s.ChangeDutyCyle(50)
		print("Rotation Speed 90%")
		sleep(2)
		r.ChangeDutyCyle(100)
		print("Rotation Speed 100%")
		sleep(2)
		
		
		
		
		


