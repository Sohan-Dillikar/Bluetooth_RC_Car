# Raspberry Pi Bluetooth RC Car

In this project, I have created a Bluetooth Controlled Car, using Raspberry Pi.  To control the Raspberry Pi, I used a Bluetooth Terminal called [Serial Bluetooth Terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=en_US).

Materials :
  - Basic Materials :
    - [Raspberry Pi](https://www.amazon.com/CanaKit-Raspberry-Starter-Premium-Black/dp/B07BCC8PK7/ref=sr_1_1_sspa?dchild=1&keywords=raspberry+pi+3&qid=1597708898&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMVJaMVVMMFQxTDJNJmVuY3J5cHRlZElkPUEwMzI5MzA0VTVHQUY5R0I3WVNKJmVuY3J5cHRlZEFkSWQ9QTA3NTAxMjAzTUIyNzBOUEVKVk9JJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
    - [Breadboard](https://www.amazon.com/EL-CP-003-Breadboard-Solderless-Distribution-Connecting/dp/B01EV6LJ7G/ref=sr_1_1_sspa?dchild=1&keywords=breadboard&qid=1597709033&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUzJGSEpMRU1TSjNLJmVuY3J5cHRlZElkPUEwODI2MDcwM0I3NjBXOUtRSUxHQyZlbmNyeXB0ZWRBZElkPUEwNTI0ODkxMTVLQVI1Vk9QVEE5OCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)
    - [Python3](https://www.python.org/)
    - RPi.GPIO Module
    - Monitor, Keyboard, Mouse
    - Android Phone or Tablet 
  - Project Components :
    - [l293d](https://www.amazon.com/PIXNOR-16-pin-Stepper-Drivers-Controllers/dp/B00ODQM8KC/ref=sr_1_1_sspa?dchild=1&keywords=l293d&qid=1597709181&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4TFVWV0FBSVVENlomZW5jcnlwdGVkSWQ9QTA0ODk2NTUxVDQ4T1FZMDNEOEhQJmVuY3J5cHRlZEFkSWQ9QTAxNTUzNDMxSzJMWVcwMFBWMExRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==) x2
    - [DC Motors + Wheels](https://www.amazon.com/Electric-Magnetic-Gearbox-Plastic-Yeeco/dp/B07DQGX369/ref=sr_1_3?dchild=1&keywords=robot+car+wheels&qid=1597709235&sr=8-3) x4 (Check out the Car Chassis below if you are interested in DC Motors + Wheels + Car Chassis + Battery Holder!)
    - [Active Buzzer](https://www.amazon.com/Cylewet-Electronic-Magnetic-Continuous-Arduino/dp/B01N7NHSY6/ref=sr_1_1_sspa?dchild=1&keywords=active+buzzer&qid=1597709289&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUU1PODFCVE5TRzJRJmVuY3J5cHRlZElkPUEwNzQ4MzIxNEhSR0hGV0M1R1kmZW5jcnlwdGVkQWRJZD1BMDU5NDkyNzMzMjVJRVNKNVBLWFQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl) x1
    - [NPN Transistor](https://www.amazon.com/MCIGICM-200pcs-Transistor-Bipolar-Transistors/dp/B06XRBLKDR/ref=sr_1_4?crid=17JKXPVKPJUL7&dchild=1&keywords=npn+transistor&qid=1597709395&sprefix=npn+transis%2Caps%2C225&sr=8-4) x1
    - [Push Button](https://www.amazon.com/Gikfun-12x12x7-3-Tactile-Momentary-Arduino/dp/B01E38OS7K/ref=sr_1_1_sspa?crid=PZ6YVWD2N7Q5&dchild=1&keywords=push+button+arduino&qid=1597709451&sprefix=push+button+ardui%2Caps%2C223&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTllZQkRRUEZFQjZOJmVuY3J5cHRlZElkPUExMDA3MzM5MVhYMVdEWk5IWDdCNyZlbmNyeXB0ZWRBZElkPUEwMTgxNTM5MlJTRzFKT01HTzhDQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) x1 (Comes with Push Button Caps!)
    - [Jumper Wires](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY/ref=sr_1_1_sspa?dchild=1&keywords=jumper+wires&qid=1597709511&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUUlNRDBDRDFUSVNZJmVuY3J5cHRlZElkPUEwMjQ2MDMyMlRQSVZVSzZZMUFCNyZlbmNyeXB0ZWRBZElkPUEwOTQ1NDM2MUpBN1RMSkJGREFMWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)
   - Optional :
     - [Car Chassis](https://www.amazon.com/perseids-Chassis-Encoder-Wheels-Battery/dp/B07DNXBFQN/ref=sr_1_2?dchild=1&keywords=robot+car+wheels&qid=1597709751&sr=8-2) x1 (Comes with 4 DC Motors and Wheels!)
     - [T-Type Breadboard Extension + Belt](https://www.amazon.com/Kuman-Expansion-Raspberry-Solderless-Breadboard/dp/B074DSMPYD/ref=sr_1_8?dchild=1&keywords=breadboard+extension&qid=1597765374&sr=8-8) (Comes with Jumper Wires and Mini Breadboard!)

Required Knowledge :
  - Basic Python3 Fundamentals
  - Flow of Current
  - Resistor Functionality
  - Trasistor Functionality
  - Wiring an l293d Motor Driver
  - Wiring an Active Buzzer
  - Wiring a Push Button
