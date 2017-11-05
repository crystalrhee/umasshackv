import serial
import re

ser = serial.Serial('/dev/cu.usbmodem1411') # open port

while True:
    fh = open("temp_data.txt","w")
    line = ser.readline()
    temp = re.search(r'\d+', line).group()
    print(temp)
    fh.write(temp);
    fh.close
