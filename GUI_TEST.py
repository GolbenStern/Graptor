import RPi.GPIO as GPIO
import tkinter as tk

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# Set up the PWM object
pwm1 = GPIO.PWM(4, 50)
pwm2 = GPIO.PWM(17, 50)
pwm3 = GPIO.PWM(27, 50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

# Create the Tkinter window
root = tk.Tk()
root.title("Servo and Solenoid Control")

# Create the slider
slider1 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Duty Cycle (%)")
slider1.pack()
slider2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Duty Cycle (%)")
slider2.pack()
slider3 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Duty Cycle (%)")
slider3.pack()

# Define a function to update the duty cycle
def update_duty_cycle1(duty_cycle):
    pwm1.ChangeDutyCycle(duty_cycle)
def update_duty_cycle2(duty_cycle):
    pwm2.ChangeDutyCycle(duty_cycle)
def update_duty_cycle3(duty_cycle):
    pwm3.ChangeDutyCycle(duty_cycle)

# Set the initial duty cycle
update_duty_cycle1(slider1.get())
update_duty_cycle2(slider2.get())
update_duty_cycle3(slider3.get())

# Configure the slider to call the update_duty_cycle function when changed
slider1.config(command=update_duty_cycle1)
slider2.config(command=update_duty_cycle2)
slider3.config(command=update_duty_cycle3)

# Start the Tkinter event loop
root.mainloop()

# Clean up the GPIO pins
pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()
