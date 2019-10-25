import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

x = 0
for x in range(10):

	GPIO.output(12, GPIO.HIGH)
	time.sleep(2)

	GPIO.output(12, GPIO.LOW)
	time.sleep(1)

	x = x+1

GPIO.cleanup()
