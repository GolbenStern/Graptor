#test code top run 2 servos from keyboard inputs

import RPi.GPIO as GPIO
import time
import tkinter as tk

GPIO.setmode(GPIO.BCM)

# define servo pins
servo1_pin = 18
servo2_pin = 17

# setup servo pins as output
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)

# create servo objects
servo1 = GPIO.PWM(servo1_pin, 50)
servo2 = GPIO.PWM(servo2_pin, 50)

# start servos at 0 position
servo1.start(0)
servo2.start(0)

# create GUI window
root = tk.Tk()
root.title("Servo Control")

# function to run servo1 clockwise
def run_servo1_cw():
    servo1.ChangeDutyCycle(7.5) # turn to 90 degrees
    time.sleep(1)
    servo1.ChangeDutyCycle(12.5) # turn to 180 degrees
    time.sleep(1)
    servo1.ChangeDutyCycle(2.5) # turn to 0 degrees
    time.sleep(1)

# function to run servo1 counter-clockwise
def run_servo1_ccw():
    servo1.ChangeDutyCycle(12.5) # turn to 180 degrees
    time.sleep(1)
    servo1.ChangeDutyCycle(7.5) # turn to 90 degrees
    time.sleep(1)
    servo1.ChangeDutyCycle(2.5) # turn to 0 degrees
    time.sleep(1)

# function to stop servo1
def stop_servo1():
    servo1.ChangeDutyCycle(0)

# function to run servo2 clockwise
def run_servo2_cw():
    servo2.ChangeDutyCycle(7.5) # turn to 90 degrees
    time.sleep(1)
    servo2.ChangeDutyCycle(12.5) # turn to 180 degrees
    time.sleep(1)
    servo2.ChangeDutyCycle(2.5) # turn to 0 degrees
    time.sleep(1)

# function to run servo2 counter-clockwise
def run_servo2_ccw():
    servo2.ChangeDutyCycle(12.5) # turn to 180 degrees
    time.sleep(1)
    servo2.ChangeDutyCycle(7.5) # turn to 90 degrees
    time.sleep(1)
    servo2.ChangeDutyCycle(2.5) # turn to 0 degrees
    time.sleep(1)

# function to stop servo2
def stop_servo2():
    servo2.ChangeDutyCycle(0)

# create GUI buttons
btn_servo1_cw = tk.Button(root, text="Servo1 CW", bg="green", command=run_servo1_cw)
btn_servo1_ccw = tk.Button(root, text="Servo1 CCW", bg="red", command=run_servo1_ccw)
btn_servo1_stop = tk.Button(root, text="Servo1 Stop", bg="gray", command=stop_servo1)
btn_servo2_cw = tk.Button(root, text="Servo2 CW", bg="green", command=run_servo2_cw)
btn_servo2_ccw = tk.Button(root, text="Servo2 CCW", bg="red", command=run_servo2_ccw)
btn_servo2_stop = tk.Button(root, text="Servo2 Stop", bg="gray", command=stop_servo2)

#
