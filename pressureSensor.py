import RPi.GPIO as GPIO
from hx711 import HX711

DT = 18
SCK = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(DT, GPIO.IN)
GPIO.setup(SCK, GPIO.OUT)

hx = HX711(DT, SCK)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()
hx.tare()

while True:
    try:
        val = hx.get_weight()
        print(val)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        raise
