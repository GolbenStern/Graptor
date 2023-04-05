import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # replace '/dev/ttyACM0' with the serial port that your Arduino is connected to

time.sleep(2)  # wait for the serial connection to initialize

ser.write(b'Hello, World!')  # send the message to the Arduino

ser.close()  # close the serial connection




