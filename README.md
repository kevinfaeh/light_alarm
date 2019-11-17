# light_alarm

This is a raspberry pi project. To goal is to have a website in your local network to turn lights/switches on and off, change the color of the bulb and to set a light alarm with sound at a desired time. The alarm and light control is managed with the raspberry pi. What you need is a raspberry pi, audio device, mystrom wifi bulb and optionally a mystrom wifi switch that you want to control.

The mystrom wifi bulb and wifi switch are controlled with a web interface over an apache2 server running on the raspberry pi. The commands are python scripts which are exectued via php. In the python_scripts folder is the class WifiBulb.py and WifiSwitch.py which hold all functions.
All website dependecies are in the css, images and js folde.
To make everything run on your pi do the following:
```shell
install apache2
sudo apt-get install apache2
install php
sudo apt-get install php
```
Check if apache2 works by inserting http://localhost in your browser.

Put the light alarm folder to your desired location, e.g. /home/pi/html/light-alarm.
In /ect/apache2/sites_available edit the 000-default.conf with root previleges.
```shell
sudo nano 000-default.conf
```
Look for
```shell
"DocumentRoot /var/www/html"
``` 
or 
```shell
"DocumentRoot /var/www"
```
and change this path to your light-alarm folders path, e.g. "DocumentRoot /home/pi/html/light-alarm".

Do the same in the /etc/apache2/apache2.conf file. Look for:
```shell
<Directory /var/www/html/>
Options Indexes FollowSymLinks
AllowOverride None
Require all granted
</Directory>
```

and change "/var/www/html/" to your folders path.

Go into the folder light-alarm, e.g /home/pi/html/light-alarm and create a virtual environment:
```shell
pyhton3 -m venv env
```
Source the virtual environment with:
```shell
source env/bin/activate
```
Install the pygame package to play music over the audio jack:
```shell
pip3.7 install pygame
```
Deactivate the envoronment again.
```shell
deactivate
```

To make that music is played over the audio jack by default, enter the following:
```shell
amixer cset numid=3 1
```
or go to raspi-config:
```shell
sudo raspi-config
```
and edit in Advanced Options the Audio section.

To allow that the commands executed by apache2 (group: www-data) can play music, add them to the audio group run:
```shell
sudo usermod -aG audio www-data
```

To give the system the needed access rights over the light-alarm folder do the following
```shell
sudo chmod -R 755 /home/pi/html/light-alarm
```
then give the bulb_data.txt file full access with:
```shell
sudo chmod 777 /home/pi/html/light-alarm/pyhton_scripts/bulb_data.txt
```

Now the only thing left is to insert your WifiBulb and WifiSwitch IP and MAC address in the WifiBulb.py and WifiSwitch.py class. Look at the bottem where a bulb or switch object is instantiated and edit there the IP and MAC address of your device. The MAC address is written on the product box and the IP address can be found with your router. For the switch it is possible that you need to enable access rights read the security section in https://api.mystrom.ch/?version=latest. Paste the IP-address of your switch in the browser, and go to "Experte" in the drop-down. There activate REST API and Panel Station Modus without setting any Token.

If anything fails, checkout the error logs in /var/log/apache2/error.log . Or try to run the python scripts without web interface in the shell.

If everything works, you can now turn the light/switch on and off, change the color and set an alarm with alarm duration by inserting the IP address of your Raspberry Pi in the Browser of any device in your local network.
