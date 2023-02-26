#pip install serial
import serial
import time



ser = serial.Serial('COM6',9600,timeout=1)

ser.write(b'F')
time.sleep(1)
ser.write(b'F')
time.sleep(1)
ser.write(b'F')
time.sleep(1)
for x in range(32):
        tmp = []
        for y in range(32):
            if( x%2 ==1):
                ser.write(b'D')#d
            else:
                ser.write(b'U')#u
            ser.read()
            time.sleep(1)
            
        ser.write(b'R')
       

ser.close()
