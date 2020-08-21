import RPi.GPIO as GPIO

leftWheelPins = ((11, 13, 15), (12, 16, 18))
rightWheelPins = ((33, 35, 37), (36, 38, 40))

def setupWheels():
    for pins in leftWheelPins + rightWheelPins:
        GPIO.setup(pins[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(pins[1], GPIO.OUT)
        GPIO.setup(pins[2], GPIO.OUT)

def enablePins(pins):
    for pin_set in pins:
        GPIO.output(pin_set[0], GPIO.HIGH)

def disablePins(pins):
    for pin_set in pins:
        GPIO.output(pin_set[0], GPIO.LOW)

def rightWheels(direction):
    enablePins(rightWheelPins)
    if direction == "forward":
        GPIO.output(rightWheelPins[0][1], GPIO.HIGH)
        GPIO.output(rightWheelPins[0][2], GPIO.LOW)
        GPIO.output(rightWheelPins[1][1], GPIO.LOW)
        GPIO.output(rightWheelPins[1][2], GPIO.HIGH)
    elif direction == "backward":
        GPIO.output(rightWheelPins[0][1], GPIO.LOW)
        GPIO.output(rightWheelPins[0][2], GPIO.HIGH)
        GPIO.output(rightWheelPins[1][1], GPIO.HIGH)
        GPIO.output(rightWheelPins[1][2], GPIO.LOW)
    else:
        disablePins(rightWheelPins)

def leftWheels(direction):
    enablePins(leftWheelPins)
    if direction == "forward":
        GPIO.output(leftWheelPins[0][1], GPIO.LOW)
        GPIO.output(leftWheelPins[0][2], GPIO.HIGH)
        GPIO.output(leftWheelPins[1][1], GPIO.LOW)
        GPIO.output(leftWheelPins[1][2], GPIO.HIGH)
    elif direction == "backward":
        GPIO.output(leftWheelPins[0][1], GPIO.HIGH)
        GPIO.output(leftWheelPins[0][2], GPIO.LOW)
        GPIO.output(leftWheelPins[1][1], GPIO.HIGH)
        GPIO.output(leftWheelPins[1][2], GPIO.LOW)
    else:
        disablePins(leftWheelPins)

def forward(wheels):
    if wheels == "right-wheels":
        rightWheels("forward")
    elif wheels == "left-wheels":
        leftWheels("forward")
    else:
        rightWheels("forward")
        leftWheels("forward")

def backward(wheels):
    if wheels == "right-wheels":
        rightWheels("backward")
    elif wheels == "left-wheels":
        leftWheels("backward")
    else:
        rightWheels("backward")
        leftWheels("backward")

def stop(wheels):
    if wheels == "right-wheels":
        rightWheels("stop")
    elif wheels == "left-wheels":
        leftWheels("stop")
    else:
        rightWheels("stop")
        leftWheels("stop")

def turn(direction):
    if direction == "right":
        forward("left-wheels")
        backward("right-wheels")
    else:
        forward("right-wheels")
        backward("left-wheels")
