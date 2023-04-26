import RPi.GPIO as GPIO
import tkinter as tk

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Set up the PWM object
pwm = GPIO.PWM(18, 50)
pwm.start(0)

# Create the Tkinter window
root = tk.Tk()
root.title("Servo Control")

# Create the slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Duty Cycle (%)")
slider.pack()

# Define a function to update the duty cycle
def update_duty_cycle(duty_cycle):
    pwm.ChangeDutyCycle(duty_cycle)

# Set the initial duty cycle
update_duty_cycle(slider.get())

# Configure the slider to call the update_duty_cycle function when changed
slider.config(command=update_duty_cycle)

# Start the Tkinter event loop
root.mainloop()

# Clean up the GPIO pins
pwm.stop()
GPIO.cleanup()
