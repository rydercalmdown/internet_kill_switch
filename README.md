# Internet Kill Switch
Physical switches for turning off websites, similar to a pi-hole, but for specific stuff.


## Architecture
This project is mostly powered by dnsmasq, which takes care of all the upstream DNS forwarding and blocking of specific domains. There's a small python script that runs on boot and manages the config files for dnsmasq - listening for changes in GPIO state and updating config.

## Installation
Clone the repository on your raspberry pi - I'm using a raspberry pi zero, but as long as it has WiFi it should work:

```
cd ~/
git clone https://github.com/rydercalmdown/internet_kill_switch
```

Descend into the directory, and run the installation command:
```bash
cd internet_kill_switch
make install
```

To run temporarily, use the following command:
```bash
make run
```

To run on boot, add the following lines to the /etc/rc.local file, just before the last line.

```bash
sudo nano /etc/rc.local

# Add this line before the last line
cd /home/pi/internet_kill_switch/src && sudo ../env/bin/python app.py &
```

Or, just run the following command, which will make the changes for you.
```bash
make configure-on-boot
```


## Pin Diagram
You can specify your pins for this project in the toggle_switches.py file. This project uses Broadcom (BCM) numbering, so the numbers on the outside of this diagram (GPIO14 becomes 14 etc.).


![Pin diagram](/misc/pin_layout.svg)
