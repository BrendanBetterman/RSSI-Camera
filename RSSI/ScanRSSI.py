import serial
import sys
sys.path.insert(1,'../ImageProcessing')
import image

import subprocess
import time
from csv import writer

def avgList(rssi):
    out = 0
    for i in rssi:
        out += int(i)
    return out/len(rssi)
def getSlow():
    output = subprocess.getoutput("iw wlp4s0 scan | grep '\\bsignal:\|\\bfreq:'")
    
    #output = subprocess.getoutput("iw wlp4s0 scan | grep '\\bsignal:\|\\bSSID:\|\\bfreq:")
    
    outputList = output.split("\n")
    freq = []
    signal = []
    #ssid = []
    for i in range(0,len(outputList),2):
        freq.append(int(outputList[i].split(" ")[1]))
        if freq[len(freq)-1] <=5000.0: 
            signal.append(float(outputList[i+1].split(" ")[1]))
        
        #ssid.append(outputList[i+2])
    return avgList(signal)
def getRssi():
    output = subprocess.getoutput("nmcli dev wifi")
    outputlist = output.split("\n")
    rate = []
    signal = []
    outputlist.pop(0)
    for router in outputlist:
        cols = router.split()
        #adjust for spaces in ssids
        signalloc = 6
        for i in range(5,len(cols)):
            if cols[i] == "Mbit/s":
                signalloc = i+1
                break
        signal.append(cols[signalloc])
        rate.append(cols[signalloc-2])
    return avgList(signal)

def main():
    fileName = 'wifi-' + str(time.strftime('%Y-%m-%d-%H:%M:%S')) 
    print(fileName)
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    output = []
    size = 16
    percentage = 0
    turn = 100/(size*size) 
    start = time.time()
    for x in range(size):
        tmp = []
        for y in range(size):
            if( x%2 ==1):
                ser.write(b'D')
            else:
                ser.write(b'U')
            tmp.append(getRssi())
            #tmp.append(getSlow())
            time.sleep(2)
            ser.read()
            percentage += turn
            elapsedTime = (time.time() - start)
            estimateTime = elapsedTime/(percentage/100) 
            remaining = estimateTime- elapsedTime
            print(str(round(percentage,2)) + "%      " + str(round(remaining,2)) + "Seconds", end='\r')
        ser.write(b'R')
        output.append(tmp)
        ser.read()
    end = time.time()
    #print(output)
    print("\n")
    with open(fileName+ '.csv','a') as f_object:
        writer_object = writer(f_object)
        for i in output:
            writer_object.writerow(i)
        f_object.close()
    image.csvToImage(fileName)
    print(end-start)
    for x in range(size):
        ser.write(b'L')
        ser.read()
main()
