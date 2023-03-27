#this code is for inputting the output for gpio pin 18 to control the solenoid as a test
#this code is not for final user

import RPi.GPIO as GPIO

# Set up GPIO pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    # Wait for user input
    user_input = input("Press r to activate GPIO pin 18, or s to stop it: ")
    
    if user_input == "r":
        # Activate GPIO pin 18
        GPIO.output(18, GPIO.HIGH)
    elif user_input == "s":
        # Stop GPIO pin 18
        GPIO.output(18, GPIO.LOW)
