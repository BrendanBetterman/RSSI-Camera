from PIL import Image
import numpy as np

CSV = open("wifi.csv")
wifidata = np.loadtxt(CSV,delimiter=",")

out_image = np.zeros((len(wifidata[0]),len(wifidata),3),dtype=np.uint8)
for x in range(len(wifidata[0])-1):
       for y in range(len(wifidata)-1):
              if (y%2 ==0):
                    rssi = wifidata[y,x]
              else:
                    rssi = wifidata[y,len(wifidata[0])-x-1]  
              normalized = (rssi-30)/(30-100)
              red = 1/normalized *255
              green = normalized*255
              pixel = [red,green,0]
              out_image[x,y]=pixel
out = Image.fromarray(out_image.astype(np.uint8))
out.save('test2.png')