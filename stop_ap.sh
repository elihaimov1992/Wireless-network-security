#!/usr/bin/bash

sudo systemctl stop hostapd 
sudo systemctl stop dnsmasq 
sudo killall dnsmasq
sudo killall hostapd