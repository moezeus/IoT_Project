# Here is the configuration:
# Connect the servo voltage pin to Rpi 5v
# Connect the servo GND pin to Rpi GND
# Connect the servo signal pin to GPIO17 (pin 11)

import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.ChangeDutyCycle(5)

while True: 
    p.start(6.7)
    time.sleep(0.7)
    p.start(7)
    time.sleep(0.7)
    p.start(7.4)
    time.sleep(0.7)
    p.start(7)
    time.sleep(0.7)