# espModeStirring
Files for controlling ESP-301-3N Motion Controller with python through a serial port

USB config 921600 baud rate, 8 data bits, N parity, 1 stop bit

ESP-301-3N Motion Controller connected to 2 IMS 600-pp motion stages

https://www.newport.com/medias/sys_master/images/images/hda/h3e/9117547069470/ESP301-User-s-Manual.pdf

# Seting up serial to usb connection to your windows x64 machine
1. Download the entire github repository as zip as shown in "download github repository" which is located in esp301 setup tutorial file
2. Open device manager and locate ESP301 motion controller, probably under "other devices". Shown in "Findespindevmanager"
3. Click "update driver" and then select "browse my computer for drivers" and find the driver file located in this repository, that you downloaded as per step 1 (other drivers are available via https://www.newport.com/p/ESP301-3N). Shown in "find64-bitdriverfile"
4. ESP301 should be installed correctly now
5. In your python environment run "pip uninstall serial"
6. Run "pip install pyserial"
7. The last two steps prevent a lot of headaches when using pyserial, if it still doesn't work, run 'pip install --upgrade --force-reinstall pyserial'
8. *important* When initializing the pySerial object to send commands to the ESP301 you will refer to its port name. It defaulted to COM3 in the lab, but defaulted to COM7 on my personal laptop. To solve this I changed COM3 to COM7 in both the espModeStirring class initialization function and the call on it via "espModeStirring.espModeStirring()" in each initialization of the class. Shown in "namedcom7"
9. Now you should be able to run esp301 mulit-position 2 axis motion
