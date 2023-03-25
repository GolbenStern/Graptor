import pigpio
import time

# Set up pigpio and servo pin
pi = pigpio.pi()
servo_pin = 18
pi.set_mode(servo_pin, pigpio.OUTPUT)

# Define servo parameters
servo_min = 500
servo_max = 2500
servo_mid = int((servo_max - servo_min) / 2) + servo_min
servo_current = servo_mid

# Define servo movement functions
def servo_rotate_clockwise():
    global servo_current
    if servo_current < servo_max:
        servo_current += 50
    pi.set_servo_pulsewidth(servo_pin, servo_current)
    time.sleep(0.02)

def servo_rotate_counter_clockwise():
    global servo_current
    if servo_current > servo_min:
        servo_current -= 50
    pi.set_servo_pulsewidth(servo_pin, servo_current)
    time.sleep(0.02)

while True:
    # Wait for user input
    user_input = input("Press r to turn servo clockwise, or l to turn it counter-clockwise: ")
    
    if user_input == "r":
        # Rotate servo clockwise
        servo_rotate_clockwise()
    elif user_input == "l":
        # Rotate servo counter-clockwise
        servo_rotate_counter_clockwise()
