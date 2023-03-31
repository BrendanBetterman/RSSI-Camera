# RSSI-Camera
Using stepper motors to move an antenna to get the RSSI in different areas generating an image. This uses a Wi-Fi card so 2.4ghz and 5ghz signals are detected.
This currently only works on linux machines and was only tested on Arch Linux. <br>
<p align="center">
  <img src="https://github.com/BrendanBetterman/RSSI-Camera/blob/main/ImageProcessing/test.png" width="255" title="First Image"  style="image-rendering: crisp-edges;" >
</p>

-----------
## Libraries Needed<br />
https://github.com/BrendanBetterman/aircrack-ng <br/>
Custom aircrack-ng, this program makes a discrete result the orignal makes a continueous result. you will need to compile and install this.<br/>  


Arch Linux<br />
```
sudo pacman -S networkmanager
sudo pacman -S wireless_tools
###For Slower but more accurate also install
sudo pacman -S iw
```
Linux
```
sudo apt-get install network-manager
###For Slower but more accurate also install
sudo apt-get -y install iw
```
Python Libraries
```
pip install pyserial
pip install python-csv
pip install Pillow
pip install numpy
```
When using the slow version the python program will require a sudo since iw requires it. My WIFI card is wlp5s0 but yours may be different.<br/>
Use this command to find your access point and replace [wlp5s0](https://github.com/BrendanBetterman/RSSI-Camera/blob/ea77a924072423a8c0ed69be213c98cc22420798/RSSI/GetRSSI.py#L13)
```
iwconfig
```
------------
## Parts used<br />

### Wire <br/>
22gauge stranded wire for the rg-59 (RG59 Coax Cable Recommended Coax cable isolates noise)<br/>
Unwrapped 6 AWG Stranded Bare Copper wire 5ft in length(15ft of 16AWG Solid core 6 AWG is readliy available.)<br/>
### Motors<br/>
28BYJ-48 (Small cheap Stepper motors any uniphase steppers should work with this code)<br/>
SBTO811 (Driver)<br/>
### 3D Models<br/>
[Antenna](https://www.thingiverse.com/thing:3130541)</br>
Other models exist but are still a WIP
### Control Boards<br/>
Ardiuno nano(Any Ardiuno can be used)<br/>
