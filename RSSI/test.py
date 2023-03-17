import time
import sys
import subprocess
def airHack():
    data = []
    while len(data)<=5:
        a = subprocess.getoutput("../../../a.out")
        print(a)
        data = (a.split("\n"))
    output = []
    #print(data[3].split()[1])
    #print(len(data))
    for i in range(2,len(data)-2):
        tmp = data[i].split()[1]
        if len(tmp) <=3:
            output.append(int(data[i].split()[1]))
        else:
            output.append(int(data[i].split()[2]))
    return output
def main():
    print(airHack())
main()

