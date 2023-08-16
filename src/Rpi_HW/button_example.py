# Here is the configuration:
# Connect your button NO pin to GPIO 18 (pin 12)
# Connect your button COM pin to GND

from gpiozero import Button

button = Button(18, bounce_time=1)

while True: 
    if button.is_pressed: 
        print("button pressed")
    else: 
        print("button released")