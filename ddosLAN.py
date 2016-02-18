from scapy.all import *
import netaddr

# Define IP range 
network = "172.30.4.0/28"

try:
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network),inter=0.05,timeout=0.5)
    
    for r in unans:
        print r[ARP].pdst
        
    
except KeyboardInterrupt:
    print "[*] Exiting...."
    exit(0)






