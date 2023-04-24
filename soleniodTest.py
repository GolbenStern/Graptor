import RPi.GPIO as GPIO
import Tkinter as tk
import rospy

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

        self.slider1 = tk.Scale(master, from_=6.5, to=2.5, resolution=0.1, label="Thumb Servo", command=self.run_servo1)
        self.slider1.pack()

        self.slider2 = tk.Scale(master, from_=6.5, to=2.5, resolution=0.1, label="Ring Servo", command=self.run_servo2)
        self.slider2.pack()

        self.slider3 = tk.Scale(master, from_=12.5, to=7.5, resolution=0.1, label="Index Servo", command=self.run_servo3)
        self.slider3.pack()

        self.buttons = []
        for i in range(8):
            button = tk.Button(master, text="Solenoid {}".format(i+1), bg="white", command=lambda pin=solenoid_pins[i]: self.toggle_solenoid(pin))
            button.pack()
            self.buttons.append(button)

        # Set up ROS node and subscriber
        rospy.init_node('solenoid_controller')
        rospy.Subscriber('shutdown_solenoids', Bool, self.shutdown_solenoids)

    def run_servo1(self, duty_cycle):
        servo1.ChangeDutyCycle(float(duty_cycle))

    def run_servo2(self, duty_cycle):
        servo2.ChangeDutyCycle(float(duty_cycle))

    def run_servo3(self, duty_cycle):
        servo3.ChangeDutyCycle(float(duty_cycle))

    def toggle_solenoid(self, pin):
        GPIO.output(pin, not GPIO.input(pin))

    def shutdown_solenoids(self, data):
        if data.data:
            for pin in solenoid_pins:
                GPIO.output(pin, GPIO.LOW)

root = tk.Tk()
app = App(root)
root.mainloop()

servo1.stop()
servo2.stop()
servo3.stop()
GPIO.cleanup()
