#!/usr/bin/python

# pystatus_client.py
# Run this program on the server(s) you would like to monitor.

#### Client Configuration ####

# IP to bind pystatus_client on
IP = "0.0.0.0"
# Port for pystatus_client to run on
PORT = 7000
# Path for disk info
DISK = "/"
# Device for network info
NETWORK = "eth0"
# Keep the password on pystatus_client and pystatus_server the same
PASSWORD = "yolo"

#### End configuration ####

import socket
import platform
import os
import time
import atexit
import simplejson as json

import psutil

def get_status():
    net_before = psutil.network_io_counters(pernic=True)[NETWORK]
    time.sleep(1)
    net_after = psutil.network_io_counters(pernic=True)[NETWORK]

    STATUS = json.dumps(
    {
        "hostname":platform.node(),
        "dist":platform.dist(),
        "results":[
        {
            "cpu":[
            {
                "load":os.getloadavg(),
            }],
            "memory":[psutil.virtual_memory()],
            "disk":[psutil.disk_usage(DISK)],
            "network":[
            {
                "before":net_before,
                "after":net_after
            }],
        }]
    }
    )
    return STATUS

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind((IP,PORT))

print "pystatus_client is listening on %s:%s." % (IP, PORT)
print "Use CTRL-C to exit."

try:
    while True:
        data, addr = s.recvfrom(1024)
        if data == PASSWORD:
            print "Data requested from %s:%s." % addr
            s.connect(addr)
            s.send(get_status())
            print "Data sent."
except KeyboardInterrupt:
    print "\nShutting down socket server..."
    s.close()
    print "Goodbye!"