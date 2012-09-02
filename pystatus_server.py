#!/usr/bin/python

# pystatus_client.py
# Run this program on the server that will monitor your other servers.

#### Server Configuration ####

# IP to bind pystatus_server on
IP = "0.0.0.0"
# Port for pystatus_server to run on
PORT = 7001
# Keep the password on pystatus_client and pystatus_server the same
PASSWORD = "secretpassword"
# Timeout to get information from a client
TIMEOUT = 3

# Clients you want to monitor running pystatus_client
# Use the IP and Port pystatus_client is running on

#### **** YOU MUST EDIT THIS OR IT WILL NOT WORK **** ####

CLIENTS = ['1.2.3.4:7000']

#### End configuration ####

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.settimeout(TIMEOUT)
s.bind((IP, PORT))

for client in CLIENTS:
    try:
        print client.split(':')[0]
        s.connect((client.split(':')[0], int(client.split(':')[1])))
        s.send(PASSWORD)
        data, addr = s.recvfrom(1024)
        print data
    except:
        print "Request timed out, client not \
responding, or wrong password."

s.close()
