from hx711 import HX711
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Set the HX711 pins on the microcontroller
hx = HX711(dout_pin=18, pd_sck_pin=17)

while True:
    reading = hx.get_raw_data_mean()
    print(reading)