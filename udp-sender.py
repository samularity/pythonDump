#!/usr/bin/env python3
#UDP Sender
import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"
  
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
  
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
b = bytearray()
b.extend(map(ord, MESSAGE))
sock.sendto(b, (UDP_IP, UDP_PORT)) 