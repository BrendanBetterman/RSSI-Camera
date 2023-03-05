#pip install serial
import serial
import time



ser = serial.Serial('COM7',9600,timeout=1)

ser.write(b'F')
time.sleep(1)
ser.write(b'F')
time.sleep(1)
ser.write(b'F')
time.sleep(1)
for x in range(16):
        tmp = []
        for y in range(16):
            if( x%2 ==1):
                ser.write(b'D')#d
            else:
                ser.write(b'U')#u
                
            ser.read()
            #time.sleep(1)
            
        ser.write(b'R')
        ser.read()
for x in range(16):
     ser.write(b'L')
     ser.read()
     
ser.close()
