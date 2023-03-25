#test code top run 2 servos from keyboard inputs

import RPi.GPIO as GPIO
import time

# Set up GPIO and servo pins
GPIO.setmode(GPIO.BCM)
servo_pin_1 = 18
servo_pin_2 = 19
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)

# Define servo parameters
servo_min = 500
servo_max = 2500
servo_mid = int((servo_max - servo_min) / 2) + servo_min
servo_current_1 = servo_mid
servo_current_2 = servo_mid

# Define servo movement functions
def servo_rotate_clockwise(servo_pin, servo_current):
    if servo_current < servo_max:
        servo_current += 50
    GPIO.output(servo_pin, GPIO.HIGH)
    time.sleep(servo_current / 1000000.0)
    GPIO.output(servo_pin, GPIO.LOW)
    time.sleep(0.02 - servo_current / 1000000.0)
    return servo_current

def servo_rotate_counter_clockwise(servo_pin, servo_current):
    if servo_current > servo_min:
        servo_current -= 50
    GPIO.output(servo_pin, GPIO.HIGH)
    time.sleep(servo_current / 1000000.0)
    GPIO.output(servo_pin, GPIO.LOW)
    time.sleep(0.02 - servo_current / 1000000.0)
    return servo_current

while True:
    # Wait for user input
    user_input = input("Press r to turn servo 1 clockwise, or l to turn it counter-clockwise. Press d to turn servo 2 clockwise, or m to turn it counter-clockwise: ")
    
    if user_input == "r":
        # Rotate servo 1 clockwise
        servo_current_1 = servo_rotate_clockwise(servo_pin_1, servo_current_1)
    elif user_input == "l":
        # Rotate servo 1 counter-clockwise
        servo_current_1 = servo_rotate_counter_clockwise(servo_pin_1, servo_current_1)
    elif user_input == "d":
        # Rotate servo 2 clockwise
        servo_current_2 = servo_rotate_clockwise(servo_pin_2, servo_current_2)
    elif user_input == "m":
        # Rotate servo 2 counter-clockwise
        servo_current_2 = servo_rotate_counter_clockwise(servo_pin_2, servo_current_2)
