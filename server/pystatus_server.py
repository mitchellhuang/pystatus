#!/usr/bin/python

# pystatus_server.py
# Run this program on the server that will monitor your other servers.

#### Server Configuration ####

# IP to bind pystatus_server on
IP = "0.0.0.0"
# Port for pystatus_server to run on
PORT = 7001
# Keep the password on pystatus_client and pystatus_server the same
PASSWORD = "secretpassword"
# Timeout to get information from a client
TIMEOUT = 2

# Clients you want to monitor running pystatus_client
# Use the IP and Port pystatus_client is running on

#### **** YOU MUST EDIT THIS OR IT WILL NOT WORK **** ####

CLIENTS = ["peach.huang.mx:7000", "ny.redditeast.com:7000"]

#### End configuration ####

import socket

def get_status(id):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.settimeout(TIMEOUT)
    s.bind((IP, PORT))
    try:
        print CLIENTS[id].split(":")[0]
        s.connect((CLIENTS[id].split(":")[0], int(CLIENTS[id].split(":")[1])))
        s.send(PASSWORD)
        data, addr = s.recvfrom(1024)
        return data
    except:
        return "Request timed out, client not responding, or wrong password."
    s.close()

from bottle import route, run, view, static_file

@route("/")
@view("index.tpl")
def index():
    return dict(clients=range(len(CLIENTS)))

@route("/status/<id:int>")
def status(id):
    return get_status(id)

@route("/load.gif")
def server_static():
    return static_file("load.gif", root="./")

@route("/check.gif")
def server_static():
    return static_file("check.gif", root="./")

run(host="localhost", port=8080, reloader=True)