#test code top run 2 servos from keyboard inputs

import RPi.GPIO as GPIO
import tkinter as tk

servo_pin1 = 18
servo_pin2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)

servo1 = GPIO.PWM(servo_pin1, 50)
servo2 = GPIO.PWM(servo_pin2, 50)

servo1.start(0)
servo2.start(0)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Servo Control")

        self.clockwise_button1 = tk.Button(master, text="Clockwise 1", bg="green", command=self.run_clockwise1)
        self.clockwise_button1.pack(side=tk.LEFT)

        self.counterclockwise_button1 = tk.Button(master, text="Counterclockwise 1", bg="red", command=self.run_counterclockwise1)
        self.counterclockwise_button1.pack(side=tk.LEFT)

        self.stop_button1 = tk.Button(master, text="Stop 1", bg="yellow", command=self.run_stop1)
        self.stop_button1.pack(side=tk.LEFT)

        self.clockwise_button2 = tk.Button(master, text="Clockwise 2", bg="green", command=self.run_clockwise2)
        self.clockwise_button2.pack(side=tk.LEFT)

        self.counterclockwise_button2 = tk.Button(master, text="Counterclockwise 2", bg="red", command=self.run_counterclockwise2)
        self.counterclockwise_button2.pack(side=tk.LEFT)

        self.stop_button2 = tk.Button(master, text="Stop 2", bg="yellow", command=self.run_stop2)
        self.stop_button2.pack(side=tk.LEFT)

    def run_clockwise1(self):
        servo1.ChangeDutyCycle(7.5)

    def run_counterclockwise1(self):
        servo1.ChangeDutyCycle(2.5)

    def run_stop1(self):
        servo1.ChangeDutyCycle(5)

    def run_clockwise2(self):
        servo2.ChangeDutyCycle(7.5)

    def run_counterclockwise2(self):
        servo2.ChangeDutyCycle(2.5)

    def run_stop2(self):
        servo2.ChangeDutyCycle(5)

root = tk.Tk()
app = App(root)
root.mainloop()

servo1.stop()
servo2.stop()
GPIO.cleanup()
