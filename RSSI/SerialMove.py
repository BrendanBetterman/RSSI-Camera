#pip install serial
import serial

ser = serial.Serial('COM3',9600,timeout=1)
for i in range(512):
    ser.write(b'R')
    print(ser.readline())

ser.close()
