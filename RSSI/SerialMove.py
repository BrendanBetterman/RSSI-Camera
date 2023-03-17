#pip install serial
import serial
import time



ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)


for x in range(16):
        tmp = []
        for y in range(16):
            if( x%2 ==1):
                ser.write(b'D')#d
            else:
                ser.write(b'U')#u
            time.sleep(0.5)    
            ser.read()
            #time.sleep(1)
            
     
ser.close()
