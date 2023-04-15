import Tkinter as tk
import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
servo_pins = [2, 3, 4]
solenoid_pins = [5, 6, 7, 8, 9, 10, 11, 12]

for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
for pin in solenoid_pins:
    GPIO.setup(pin, GPIO.OUT)

# Define servo angles and solenoid labels
servo_angles = {"thumb": 0, "index": 0, "ring": 0}
solenoid_labels = ["1a", "1b", "2a", "2b", "3a", "3b", "4a", "4b"]

# Define functions for servo and solenoid control
def set_servo_angle(servo, angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pins[servo], True)
    pwm = GPIO.PWM(servo_pins[servo], 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.stop()
    GPIO.output(servo_pins[servo], False)

def set_solenoid_state(solenoid, state):
    GPIO.output(solenoid_pins[solenoid], state)

# Define functions for GUI control
def update_servo_angle(servo):
    angle = servo_angles[servo]
    set_servo_angle(servo_pins.index(servo), angle)
    print(f"{servo} angle set to {angle}")

def update_solenoid_state(solenoid):
    state = solenoid_states[solenoid]
    set_solenoid_state(solenoid_labels.index(solenoid), state)
    print(f"{solenoid} state set to {state}")

# Create GUI
root = tk.Tk()
root.title("Robotic Hand Control")

# Create servo angle labels
tk.Label(root, text="Thumb").grid(row=0, column=0)
tk.Label(root, text="Index").grid(row=1, column=0)
tk.Label(root, text="Ring").grid(row=2, column=0)

# Create servo angle sliders
thumb_slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, command=lambda x: servo_angles.update({"thumb": int(x)}))
thumb_slider.set(servo_angles["thumb"])
thumb_slider.grid(row=0, column=1)

index_slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, command=lambda x: servo_angles.update({"index": int(x)}))
index_slider.set(servo_angles["index"])
index_slider.grid(row=1, column=1)

ring_slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, command=lambda x: servo_angles.update({"ring": int(x)}))
ring_slider.set(servo_angles["ring"])
ring_slider.grid(row=2, column=1)

# Create solenoid buttons
solenoid_states = {solenoid: False for solenoid in solenoid_labels}

for i, solenoid in enumerate(solenoid_labels):
    tk.Button(root, text=solenoid, command=lambda s=solenoid: solenoid_states.update({s: not solenoid_states[s]})).grid(row=3, column=i+1)

# Start main loop
root.mainloop()

# Clean up GPIO
GPIO.cleanup()
