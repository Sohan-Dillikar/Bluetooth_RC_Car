import RPi.GPIO as GPIO
from time import sleep

buzzerPin = 32

def setupBuzzer():
	GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)
	
def beep():
	GPIO.output(buzzerPin, GPIO.HIGH)
	sleep(0.5)
	GPIO.output(buzzerPin, GPIO.LOW)