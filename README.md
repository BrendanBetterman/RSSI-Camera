# RSSI-Camera
Using stepper motors to move an antenna to get the RSSI in different areas generating an image. This uses a Wi-Fi card so 2.5ghz and 5ghz signals are detected.
This currently only works on linux machines and was only tested on Arch Linux. 


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
