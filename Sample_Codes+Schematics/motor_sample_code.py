import RPi.GPIO as GPIO
from time import sleep

motor1Pins = (40, 38, 36)
motor2Pins = (33, 35, 37)

def forward():
    for pinSet in motor1Pins + motor2Pins:
        GPIO.output(pinSet[0], GPIO.HIGH)
        GPIO.output(pinSet[1], GPIO.HIGH)
        GPIO.output(pinSet[2], GPIO.LOW)

def backward():
    for pinSet in motor1Pins + motor2Pins:
        GPIO.output(pinSet[0], GPIO.HIGH)
        GPIO.output(pinSet[1], GPIO.LOW)
        GPIO.output(pinSet[2], GPIO.HIGH)

def stop():
    GPIO.output(motor1Pins[0], GPIO.LOW)
    GPIO.output(motor2Pins[0], GPIO.LOW)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor1Pins + motor2Pins, GPIO.OUT, initial=GPIO.LOW)

def loop():
    while True:
        forward()
        sleep(3)
        backward(3)
        stop()
        sleep(3)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Bye!")
    finally:
        destroy()