#iw wlp5s0 scan | grep '\bsignal:\|\bSSID:\|\bfreq:'
#import os
#os.system("iw wlp5s0 scan | grep '\bsignal:\|\bSSID:\|\bfreq:'")
#import subprocess
#cmd = ['iw wlp5s0 scan']
#result = subprocess.run(cmd,stdout=subprocess.PIPE)

#result = subprocess.run(["iw wlp5s0 scan | grep '\bsignal:\|\bSSID:\|\bfreq:'", '-l'], stdout=subprocess.PIPE)
#print(result.stdout)
import subprocess
import time
''' slow but more accurate
output = subprocess.getoutput("iw wlp5s0 scan | grep '\\bsignal:\|\\bSSID:\|\\bfreq:'")
outputList = output.split("\n")
freq = []
signal = []
ssid = []
for i in range(0,len(outputList),3):
    freq.append(int(outputList[i].split(" ")[1])/1000)
    signal.append(float(outputList[i+1].split(" ")[1]))
    ssid.append(outputList[i+2])
print(signal)
print(freq)
print(ssid)
''' 
#Fast but less accurarte 66%
start = time.time()
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
end = time.time()
print(end-start)
print(signal)
print(rate)
