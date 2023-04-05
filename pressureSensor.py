from hx711 import HX711
import RPi.GPIO as GPIO

# Set the HX711 pins on the microcontroller
hx = HX711(dout_pin=18, pd_sck_pin=17)

# Calibrate the sensor and set the scale ratio
hx.set_reference_unit(1) # 1 gram
hx.tare()

# Read the weight data from the sensor
weight = hx.get_weight()
print("Weight: {} grams".format(weight))