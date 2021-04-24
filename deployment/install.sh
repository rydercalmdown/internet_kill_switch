#!/bin/bash
# install.sh
# Install dnsmasq and set up basics

sudo apt-get update
sudo apt-get install -y dnsmasq python-pip python3-pip python3-gpiozero
sudo systemctl start dnsmasq
sudo systemctl enable dnsmasq
sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.original

cd ../
python3 -m pip install virtualenv
python3 -m virtualenv -p python3 env
. env/bin/activate
pip install -r src/requirements.txt
