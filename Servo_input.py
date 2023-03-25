import RPi.GPIO as GPIO
import time

servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

try:
    while True:
        # Check for input from the terminal without waiting for an enter key
        input_char = None
        while input_char not in ['q', 'e', '']:
            input_char = input()
        
        # Set the servo position based on the input
        if input_char == 'q':
            servo.ChangeDutyCycle(7.5) # turn clockwise to 90 degrees
        elif input_char == 'e':
            servo.ChangeDutyCycle(2.5) # turn counterclockwise to 0 degrees
        else:
            servo.ChangeDutyCycle(5) # stop moving
        
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

