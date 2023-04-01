import RPi.GPIO as GPIO
import Tkinter as tk

# Set up servo on GPIO pin 18
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

# Set up solenoid on GPIO pin 16
solenoid_pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoid_pin, GPIO.OUT)

# Set up secondary solenoid on GPIO pin 17
secondary_solenoid_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(secondary_solenoid_pin, GPIO.OUT)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Servo and Solenoid Control")

        self.clockwise_button = tk.Button(master, text="Clockwise", bg="green", command=self.run_clockwise)
        self.clockwise_button.pack(side=tk.LEFT)

        self.counterclockwise_button = tk.Button(master, text="Counterclockwise", bg="red", command=self.run_counterclockwise)
        self.counterclockwise_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Stop", bg="yellow", command=self.run_stop)
        self.stop_button.pack(side=tk.LEFT)

        self.solenoid_button = tk.Button(master, text="Solenoid", bg="blue", command=self.toggle_solenoid)
        self.solenoid_button.pack(side=tk.LEFT)

        self.secondary_solenoid_button = tk.Button(master, text="Secondary Solenoid", bg="purple", command=self.toggle_secondary_solenoid)
        self.secondary_solenoid_button.pack(side=tk.LEFT)

        self.solenoid_state = False
        self.secondary_solenoid_state = False

    def run_clockwise(self):
        servo.ChangeDutyCycle(7.5)

    def run_counterclockwise(self):
        servo.ChangeDutyCycle(2.5)

    def run_stop(self):
        servo.ChangeDutyCycle(5)

    def toggle_solenoid(self):
        self.solenoid_state = not self.solenoid_state
        GPIO.output(solenoid_pin, self.solenoid_state)

    def toggle_secondary_solenoid(self):
        self.secondary_solenoid_state = not self.secondary_solenoid_state
        GPIO.output(secondary_solenoid_pin, self.secondary_solenoid_state)

root = tk.Tk()
app = App(root)
root.mainloop()

servo.stop()
GPIO.cleanup()
