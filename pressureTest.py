import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

input_pin = 17
GPIO.setup(input_pin, GPIO.IN)

input_value = GPIO.input(input_pin)
print("Input value:", input_value)

GPIO.cleanup()