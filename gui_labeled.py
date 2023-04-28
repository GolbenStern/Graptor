import tkinter as tk
import RPi.GPIO as GPIO

# Define GPIO pins for servos and solenoids
servo_pins = [2, 3, 4]
solenoid_pins = [[23, 24], [7, 8], [6, 13], [19, 26]]

# Define ranges for servo buttons
servo_ranges = [[2.5, 3.5, 4.5, 5.5, 6.5], [12.5, 11.5, 10.5, 9.5, 8.5, 7.5], [2.5, 3.5, 4.5, 5.5, 6.5]]

# Define labels for solenoid buttons
solenoid_labels = ["Palm", "Thumb", "Index", "Ring"]

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
for pair in solenoid_pins:
    GPIO.setup(pair, GPIO.OUT)

# Function to set servo position
def set_servo_position(pin, position):
    duty = position / 10.0 + 2.5
    GPIO.output(pin, True)
    p = GPIO.PWM(pin, 50)
    p.start(duty)
    p.ChangeDutyCycle(duty)
    p.stop()

# Function to toggle solenoid
def toggle_solenoid(pin, state):
    GPIO.output(pin, state)

# Create GUI
root = tk.Tk()
root.title("Control Panel")
root.configure(background='black')

# Add servo labels and buttons
for i in range(len(servo_pins)):
    servo_label = tk.Label(root, text="Servo " + str(i+1), fg="white", bg="black")
    servo_label.grid(row=i, column=0)
    for j in range(len(servo_ranges[i])):
        button_text = str(servo_ranges[i][j])
        servo_button = tk.Button(root, text=button_text, bg="black", fg="white",
                                 command=lambda pin=servo_pins[i], pos=servo_ranges[i][j]: set_servo_position(pin, pos))
        servo_button.grid(row=i, column=j+1)

# Add solenoid labels and buttons
for i in range(len(solenoid_labels)):
    solenoid_label_pos = tk.Label(root, text=solenoid_labels[i] + " Pos", fg="white", bg="black")
    solenoid_label_pos.grid(row=i+3, column=0)
    solenoid_button_pos = tk.Button(root, text="Off", bg="black", fg="white",
                                    command=lambda i=i: toggle_solenoid(solenoid_pins[i][0], 1))
    solenoid_button_pos.grid(row=i+3, column=1)
    solenoid_label_neg = tk.Label(root, text=solenoid_labels[i] + " Neg", fg="white", bg="black")
    solenoid_label_neg.grid(row=i+3, column=2)
    solenoid_button_neg = tk.Button(root, text="Off", bg="black", fg="white",
                                    command=lambda i=i: toggle_solenoid(solenoid_pins[i][1], 1))
    solenoid_button_neg.grid(row=i+3, column=3)

root.mainloop()
