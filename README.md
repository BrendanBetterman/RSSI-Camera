# RSSI-Camera
Using stepper motors to move an antenna to get the RSSI in different areas generating an image. This uses a Wi-Fi card so 2.5ghz and 5ghz signals are detected.
This currently only works on linux machines and was only tested on Arch Linux. <br>
<p align="center">
  <img src="https://github.com/BrendanBetterman/RSSI-Camera/blob/main/ImageProcessing/test.png" width="255" title="First Image"  style="image-rendering: crisp-edges;" >
</p>

-----------
## Libraries Needed<br />
Arch Linux<br />
```
pacman -S network-manager 
pip install pyserial
###For Slower but more accurate also install
pacman -S iw
```
Linux
```
sudo apt-get install network-manager
pip install pyserial
###For Slower but more accurate also install
sudo apt-get -y install iw
```
When using the slow version the python program will require a sudo since iw requires it. My WIFI card is wlp5s0 but yours may be different.<br/>
Use this command to find your access point and replace [wlp5s0](https://github.com/BrendanBetterman/RSSI-Camera/blob/ea77a924072423a8c0ed69be213c98cc22420798/RSSI/GetRSSI.py#L13)
```
iwconfig
```
------------
## Parts used<br />

### Wire <br/>
Bell Wire for the rg-59 (RG59 Coax Cable Recommended)<br/>
Unwrapped 6 AWG Stranded Bare Copper wire 5ft in length(15ft of 16AWG Solid core 6 AWG is readliy available.)<br/>
### Motors<br/>
28BYJ-48 (Small cheap Stepper motors any uniphase steppers should work with this code)<br/>
SBTO811 (Driver)<br/>
### 3D Models<br/>
[Antenna](https://www.thingiverse.com/thing:3130541)
### Control Boards<br/>
Ardiuno nano(Any Ardiuno can be used)<br/>
