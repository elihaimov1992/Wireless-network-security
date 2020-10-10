#!/usr/bin/env python

from scapy.all import *

ap_list = []

def PacketHandler(pkt):
    if (pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp) or pkt.haslayer(Dot11)):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                mac = pkt.addr2
                bssid = pkt.addr3
                ssid = pkt.info
                channel = int(ord(pkt[Dot11Elt:3].info))
                print("AP = [MAC: %s, BSSID:%s, SSID: %s, Channel: %d]" %(mac, bssid, ssid, channel))

interface = sys.argv[1]
print("start scanning with interface: %s" %(interface))
sniff(iface=interface, prn = PacketHandler)

