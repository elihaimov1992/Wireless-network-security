# Wireless Network Security: Captive Portal Attack (Course Project)

Implementation of the captive portal attack


## Introduction

Wireless protocols have evolved drastically since 2003 after the invention of WPA in terms of secure access to Wi-Fi. Nowadays wireless networks have become a part of our daily lives. Almost every home, business, store, industry and institution has its own personal wireless AP (Access Point). Moreover, in order to make the Internet free (for free) for every detail, some organizations have set up public open Wi-Fi devices in almost every public place, such as airports, train stations, libraries, bus terminals, hotels, etc. But when it comes to security, even after applying the best security practices, the wireless network will still be less secure than the wired network.

Practical scenario: The logic behind the "Evil Twin" attack requires creating a fake access point with the same name as the targeted Wi-Fi and creating a web page to which the victim will be directed, enter his sensitive details (password) for a specific purpose (to access the Internet) and the attacker will receive and store Them in his database.


## Table of contents

> * [C-Assignment: GCC Sanitize Options](#c-assignment-gcc-sanitize-options)
> * [Introduction](#introduction)
>   * [Program Instrumentation Options](#program-instrumentation-options)
> * [Table of contents](#table-of-contents)
> * [Installation](#installation)


## Requirements

In order to run the program, there are the following requirements:

#### Hardware requirements:
 * Computer + Internet connection
 * Wireless adapter
 
#### Software requirements:
 * Kali Linux 2019.2 OS
 * Airmon-ng, Airodump-ng, Airplay-ng
 * Dnsmasq- Used to resolve requests - DNS from host. It can also act as a DHCP server
 * Iptables- Firewall used for Linux-based systems
 * Apache2- Serves as a web server for the victim. Basically it will host the phishing web page in the attacker's system
 * Hostapd- Used to create a targeted fake access point, whether it's WEP, WPA, WPA2 personal or enterprise secure


## Installation

To get started, you need to update the operating system and install the required packages in Python:
```
sudo apt-get install update
sudo apt-get install hostapd dnsmasq apache2
```
After downloading the files from this page, move all the files from the html folder to `/var/www/html`

How to run the program:
```
running modes:
    -h help
    -s scan        : Scan for Access Point\n
    -u deauth      : Deauthenticate client from Access Point\n
    -r run-ap      : Run Access Point\n
    -t stop        : Stop Access Point\n


extra variables:
    -i interface   : Select Interface
    -b bssid       : MAC address, Access Point
    -d dmac        : MAC address, Destination
    -c channel     : Access Point channel

examples:
    sudo python3 captive_portal_atk.py -s -i <interface>
    sudo python3 captive_portal_atk.py -u -i <interface> -b <bssid> -d <dmac> -c <channel>
    sudo python3 captive_portal_atk.py -r -i <interface> -c <channel> -n <ssid> -e <eth>
    sudo python3 captive_portal_atk.py -t -i <interface>annel> -n <ssid> -e <eth>")
    print("sudo python3 captive_portal_atk.py -t -i <interface>")
```
