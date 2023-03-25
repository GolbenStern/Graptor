#test runs to play with the board

    import RPi.GPIO as GPIO
import tkinter as tk

servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

class App:
    def __init__(self, master):
        self.master = master
        master.title("Servo Control")

        self.clockwise_button = tk.Button(master, text="Clockwise", bg="green", command=self.run_clockwise)
        self.clockwise_button.pack(side=tk.LEFT)

        self.counterclockwise_button = tk.Button(master, text="Counterclockwise", bg="red", command=self.run_counterclockwise)
        self.counterclockwise_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Stop", bg="yellow", command=self.run_stop)
        self.stop_button.pack(side=tk.LEFT)

    def run_clockwise(self):
        servo.ChangeDutyCycle(7.5)

    def run_counterclockwise(self):
        servo.ChangeDutyCycle(2.5)

    def run_stop(self):
        servo.ChangeDutyCycle(5)

root = tk.Tk()
app = App(root)
root.mainloop()

servo.stop()
GPIO.cleanup()
