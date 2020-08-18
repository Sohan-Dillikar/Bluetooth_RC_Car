import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12

def setup():    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(ledPin,GPIO.HIGH)
            print ("LED turned ON >>>")
        else :
            GPIO.output(ledPin,GPIO.LOW) 
            print ("LED turned OFF <<<")    

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Bye")
    finally:
        destroy()