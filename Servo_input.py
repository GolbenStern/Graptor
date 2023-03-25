import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(18, 50)  # 50 Hz frequency
pwm.start(7.5)  # Start with 90 degrees position

try:
    while True:
        # Check user input and move servo accordingly
        if input() == 'q':
            pwm.ChangeDutyCycle(2.5)  # 0 degrees
        elif input() == 'e':
            pwm.ChangeDutyCycle(12.5)  # 180 degrees
        else:
            pwm.ChangeDutyCycle(7.5)  # 90 degrees
        
        # Wait for a short time before checking input again
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm.stop()
GPIO.cleanup()
