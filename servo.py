#This code will run a servo motor on pin 17

import RPi.GPIO as GPIO
import time

servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

try:
    while True:
        servo.ChangeDutyCycle(7.5) # turn to 90 degrees
        time.sleep(1)
        servo.ChangeDutyCycle(12.5) # turn to 180 degrees
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) # turn to 0 degrees
        time.sleep(1)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()