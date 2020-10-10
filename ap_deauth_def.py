from scapy.all import *

counter = 0
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 0xc:
            counter+=1
        	print("captured total of %d deauth packets" %(counter))

interface = sys.argv[1]
print("start scanning for deauth packets with interface: %s" %(interface))
sniff(iface=interface, prn = PacketHandler)