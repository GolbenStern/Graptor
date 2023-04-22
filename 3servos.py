import RPi.GPIO as GPIO
import Tkinter as tk

servo_pin1 = 2
servo_pin2 = 3
servo_pin3 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)

servo1 = GPIO.PWM(servo_pin1, 50)
servo2 = GPIO.PWM(servo_pin2, 50)
servo3 = GPIO.PWM(servo_pin3, 50)

servo1.start(0)
servo2.start(0)
servo3.start(0)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Servo Control")

        self.buttons1 = []
        self.buttons2 = []
        self.buttons3 = []

        for i in range(11):
            duty_cycle = 2.5 + i
            button = tk.Button(master, text=str(duty_cycle), bg="white", command=lambda dc=duty_cycle: self.run_servo1(dc))
            button.pack(side=tk.LEFT)
            self.buttons1.append(button)

            button = tk.Button(master, text=str(duty_cycle), bg="white", command=lambda dc=duty_cycle: self.run_servo2(dc))
            button.pack(side=tk.LEFT)
            self.buttons2.append(button)

            button = tk.Button(master, text=str(duty_cycle), bg="white", command=lambda dc=duty_cycle: self.run_servo3(dc))
            button.pack(side=tk.LEFT)
            self.buttons3.append(button)

    def run_servo1(self, duty_cycle):
        servo1.ChangeDutyCycle(duty_cycle)

    def run_servo2(self, duty_cycle):
        servo2.ChangeDutyCycle(duty_cycle)

    def run_servo3(self, duty_cycle):
        servo3.ChangeDutyCycle(duty_cycle)

root = tk.Tk()
app = App(root)
root.mainloop()

servo1.stop()
servo2.stop()
servo3.stop()
GPIO.cleanup()
