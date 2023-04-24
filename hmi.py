import RPi.GPIO as GPIO
import tkinter as tk

servo_pin1 = 2
servo_pin2 = 3
servo_pin3 = 4
solenoid_pins = [5, 6, 7, 8, 9, 10, 11, 12]

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)
for pin in solenoid_pins:
    GPIO.setup(pin, GPIO.OUT)

servo1 = GPIO.PWM(servo_pin1, 50)
servo2 = GPIO.PWM(servo_pin2, 50)
servo3 = GPIO.PWM(servo_pin3, 50)

servo1.start(0)
servo2.start(0)
servo3.start(0)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Servo and Solenoid Control")

        self.button1_inc = tk.Button(master, text="+", bg="white", fg="black", command=lambda: self.inc_servo1())
        self.button1_inc.pack(side="left")
        self.button1_dec = tk.Button(master, text="-", bg="white", fg="black", command=lambda: self.dec_servo1())
        self.button1_dec.pack(side="left")
        self.label1 = tk.Label(master, text="Thumb Servo: 2.5")
        self.label1.pack()

        self.button2_inc = tk.Button(master, text="+", bg="white", fg="black", command=lambda: self.inc_servo2())
        self.button2_inc.pack(side="left")
        self.button2_dec = tk.Button(master, text="-", bg="white", fg="black", command=lambda: self.dec_servo2())
        self.button2_dec.pack(side="left")
        self.label2 = tk.Label(master, text="Ring Servo: 2.5")
        self.label2.pack()

        self.button3_inc = tk.Button(master, text="+", bg="white", fg="black", command=lambda: self.inc_servo3())
        self.button3_inc.pack(side="left")
        self.button3_dec = tk.Button(master, text="-", bg="white", fg="black", command=lambda: self.dec_servo3())
        self.button3_dec.pack(side="left")
        self.label3 = tk.Label(master, text="Index Servo: 7.5")
        self.label3.pack()

        self.thumb_buttons = []
        for i in range(25, 66, 1):
            button = tk.Button(master, text="{}".format(i/10), bg="white", fg="black", command=lambda value=i/10: self.set_thumb_servo(value))
            button.pack(side="left")
            self.thumb_buttons.append(button)

        self.ring_buttons = []
        for i in range(25, 66, 1):
            button = tk.Button(master, text="{}".format(i/10), bg="white", fg="black", command=lambda value=i/10: self.set_ring_servo(value))
            button.pack(side="left")
            self.ring_buttons.append(button)

        self.index_buttons = []
        for i in range(55, 96, 1):
            button = tk.Button(master, text="{}".format(i/10), bg="white", fg="black", command=lambda value=i/10: self.set_index_servo(value))
            button.pack(side="left")
            self.index_buttons.append(button)

        self.buttons = []
        for i in range(8):
            button = tk.Button(master, text="Solenoid {}".format(i+1), bg="white", fg="black", command=lambda pin=solenoid_pins[i]: self.toggle_solenoid(pin))
            button.pack()
            self.buttons.append(button)

    def inc_servo1(self):
        current_value = float(self.label1["text"].split(": ")[1])
        new_value = current_value + 0.1
        if new_value <= 6.5:
            self.label1["text"] = "Thumb Servo: {:.1f}".format(new_value)
            servo1.ChangeDutyCycle(new_value)

    def dec_servo1(self):
        current_value = float(self.label1["text"].split(": ")[1])
        new_value = current_value - 0.1
        if new_value >= 2.5:
            self.label1["text"] = "Thumb Servo: {:.1f}".format(new_value)
            servo1.ChangeDutyCycle(new_value)

def inc_servo2(self):
    current_value = float(self.label2["text"].split(": ")[1])
    new_value = current_value + 0.1
    if new_value <= 6.5:
        self.label2["text"] = "Ring Servo: {:.1f}".format(new_value)
        servo2.ChangeDutyCycle(new_value)

def dec_servo2(self):
    current_value = float(self.label2["text"].split(": ")[1])
    new_value = current_value - 0.1
    if new_value >= 2.5:
        self.label2["text"] = "Ring Servo: {:.1f}".format(new_value)
        servo2.ChangeDutyCycle(new_value)

def inc_servo3(self):
    current_value = float(self.label3["text"].split(": ")[1])
    new_value = current_value + 0.1
    if new_value <= 12.5:
        self.label3["text"] = "Index Servo: {:.1f}".format(new_value)
        servo3.ChangeDutyCycle(new_value)

def dec_servo3(self):
    current_value = float(self.label3["text"].split(": ")[1])
    new_value = current_value - 0.1
    if new_value >= 7.5:
        self.label3["text"] = "Index Servo: {:.1f}".format(new_value)
        servo3.ChangeDutyCycle(new_value)

def toggle_solenoid(self, pin):
    GPIO.output(pin, not GPIO.input(pin))



