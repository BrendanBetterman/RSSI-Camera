import serial
import subprocess
import time
def avgList(rssi):
    out = 0
    for i in rssi:
        out += int(i)
    return out/len(rssi)
def getSlow():
    output = subprocess.getoutput("iw wlp5s0 scan | grep '\\bsignal:\|\\bSSID:\|\\bfreq:'")
    outputList = output.split("\n")
    freq = []
    signal = []
    ssid = []
    for i in range(0,len(outputList),3):
        freq.append(int(outputList[i].split(" ")[1])/1000)
        signal.append(float(outputList[i+1].split(" ")[1]))
        ssid.append(outputList[i+2])
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
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    output = []
    start = time.time()
    for x in range(32):
        tmp = []
        for y in range(32):
            if( x%2 ==1):
                ser.write(b'D')
            else:
                ser.write(b'U')
            tmp.append(getRssi())
            #tmp.append(getSlow())
            ser.read()
        ser.write(b'R')
        output.append(tmp)
        ser.read()
    end = time.time()
    print(output)
    print(end-start)
    for x in range(32):
        ser.write(b'L')
        ser.read()
main()