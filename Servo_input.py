import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(18, 50)  # 50 Hz frequency
pwm.start(0)  # Start with 0% duty cycle

try:
    while True:
        # Get user input without waiting for enter key
        char = input()
        
        # Check user input and move servo accordingly
        if char == 'q':
            pwm.ChangeDutyCycle(2.5)  # 0 degrees
        elif char == 'e':
            pwm.ChangeDutyCycle(12.5)  # 180 degrees
        else:
            pwm.ChangeDutyCycle(7.5)  # 90 degrees
        
except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm.stop()
GPIO.cleanup()
