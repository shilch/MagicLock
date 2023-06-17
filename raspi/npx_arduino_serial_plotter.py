import numpy as np
import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        vals = np.array(line.split(' '))#.astype(np.float)
        print(vals[0])
