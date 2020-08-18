import RPi.GPIO as GPIO

buzzerPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(buzzerPin,GPIO.HIGH)
            print ("Buzzer turned ON >>>")
        else :
            GPIO.output(buzzerPin,GPIO.LOW)
            print ("Buzzer turned OFF <<<")

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