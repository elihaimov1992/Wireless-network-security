# captive-portal-attack
implementation of the captive portal attack

#Configure:
`apt install hostapd dnsmasq apache2`

move all the files from the html folder to `/var/www/html`

#How to run:
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
