#!/usr/bin/bash

sudo systemctl stop hostapd 
sudo systemctl stop dnsmasq 
sudo killall dnsmasq
sudo killall hostapd

sudo hostapd hostapd.conf -B
sudo dnsmasq -C dnsmasq.conf