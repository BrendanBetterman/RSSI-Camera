import serial
import sys
sys.path.insert(1,'../ImageProcessing')
import image

import subprocess
import time
from csv import writer

def airHack():
    data = []
    loopcount=0
    while len(data)<=5 and loopcount<4:
        loopcount +=1 
        a = subprocess.getoutput("../../../a.out")
        #a= subprocess.run("../../../a.out",capture_output=True,stdout=subprocess.DEVNULL)
        print(a)
        data = (a.split("\n"))
    output = []
    #print(data[3].split()[1])
    #print(len(data))
    if loopcount <4:
        for i in range(2,len(data)-2):
            tmp = data[i].split()[1]
            try:
                if len(tmp) <=3:
                    output.append(int(data[i].split()[1]))
                else:
                    output.append(int(data[i].split()[2]))
            except:
                break
        canbreak = False
        for i in output:
            if i != -1:
                canbreak = True
                break
        if canbreak:
            return output
        else:
            tmp = airHack()
         
            return tmp
    else:
        return [-120]
def bestList(rssi):
    best = -120
    for i in rssi:
        if(int(i) > best and int(i) < -30):
            best = int(i)
    return -1 * best
def avgList(rssi):
    out = 0
    for i in rssi:
        out += int(i)
    return out/len(rssi)
def getChannels():
    try:
        interface = "wlp4s0"  # Replace with your WiFi interface name
        output = subprocess.check_output(["sudo", "iwlist", interface, "scan"]).decode()
        rssi_values = {}
        current_channel = None
        isFiveG = False
        for line in output.split("\n"):
            line = line.strip()
            if line.startswith("Channel"):
                current_channel = int(line.split(":")[1])
            elif line.startswith("Frequency:"):
                isFiveG = int(line.split(":")[1].split(".")[0]) == 2
            elif line.startswith("Quality="):
                if isFiveG:
                    rssi = int(line.split("=")[2].split()[0])
                    rssi_values[current_channel] = rssi
        return rssi_values
    except:
        return getChannels()
def getAvgChannels(channeldata):
    output = 0
    for channel,rssi in channeldata.items():
        output += rssi
    return output/len(channeldata)
def getBestChannels(channeldata):
    output = -120
    for channel, rssi in channeldata.items():
        if output < rssi:
            output = rssi
    return output
def getSlow():
    output = subprocess.getoutput("iw wlp4s0 scan | grep '\\bsignal:\|\\bfreq:'")
    
    #output = subprocess.getoutput("iw wlp4s0 scan | grep '\\bsignal:\|\\bSSID:\|\\bfreq:")
    
    outputList = output.split("\n")
    freq = []
    signal = []
    #ssid = []
    try:
        for i in range(0,len(outputList),2):
            freq.append(int(outputList[i].split(" ")[1]))
            if freq[len(freq)-1] <=5000.0: 
                signal.append(float(outputList[i+1].split(" ")[1]))
    except:
        return getSlow()
        #ssid.append(outputList[i+2])
    #return 
    #print(bestList(signal))
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
    print(bestList(signal))
    #return avgList(signal)
    return bestList(signal)
def estimateTime(percentage,turn,start):
    percentage += turn
    elapsedTime = elapsedTime/(percentage/100)
    remaining = estimateTime-elapsedTime
    
def main():
    #getSlow()
    fileName = 'wifi-' + str(time.strftime('%Y-%m-%d-%H_%M_%S')) 
    print(fileName)
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    output = []
    size = 10
    percentage = 0
    turn = 100/(size*size) 
    start = time.time()
    for x in range(size):
        tmp = []
        for y in range(size):
            if( x%2 ==1):
                ser.write(b'D')
                ser.read()
                ser.write(b'D')
            else:
                ser.write(b'U')
                ser.read()
                ser.write(b'U')
            
            tmp.append(bestList(airHack()))
            #tmp.append(avgList(airHack()))
            time.sleep(0.5)
            ser.read()
            percentage += turn
            elapsedTime = (time.time() - start)
            estimateTime = elapsedTime/(percentage/100) 
            remaining = estimateTime- elapsedTime
            print(str(round(percentage,2)) + "%      " + str(round(remaining,2)) + "Seconds", end='\r')
        
        ser.write(b'R')
        ser.read()
        ser.write(b'R')
        output.append(tmp)
        ser.read()
    end = time.time()
    #print(output)
    print("\n")
    with open("csv/" + fileName+ '.csv','w') as f_object:
        writer_object = writer(f_object)
        for i in output:
            writer_object.writerow(i)
        f_object.close()
    image.csvToImage(fileName)
    print(end-start)
    for x in range(size):
        ser.write(b'L')
        ser.read()
        ser.write(b'L')
        #time.sleep(0.5)
        ser.read()
    ser.write(b'U')
    ser.read()
    ser.write(b'U')
    ser.read()
for i in range(1):
    main()
