import RPi.GPIO as GPIO
import Tkinter as tk

servo_pin1 = 18
servo_pin2 = 17
min_duty_cycle = 2.5
max_duty_cycle = 12.5

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

        self.angle1 = 0
        self.angle2 = 0
        self.speed1 = 0
        self.speed2 = 0

    def run_clockwise1(self):
        if self.angle1 + self.speed1 <= max_duty_cycle:
            self.angle1 += self.speed1
        servo1.ChangeDutyCycle(self.angle1)

    def run_counterclockwise1(self):
        if self.angle1 - self.speed1 >= min_duty_cycle:
            self.angle1 -= self.speed1
        servo1.ChangeDutyCycle(self.angle1)

    def run_stop1(self):
        servo1.ChangeDutyCycle(0)
        self.angle1 = 0
        self.speed1 = 0

    def run_clockwise2(self):
        if self.angle2 + self.speed2 <= max_duty_cycle:
            self.angle2 += self.speed2
        servo2.ChangeDutyCycle(self.angle2)

    def run_counterclockwise2(self):
        if self.angle2 - self.speed2 >= min_duty_cycle:
            self.angle2 -= self.speed2
        servo2.ChangeDutyCycle(self.angle2)

    def run_stop2(self):
        servo2.ChangeDutyCycle(0)
        self.angle2 = 0
        self.speed2 = 0

root = tk.Tk()
app = App(root)
root.mainloop()
