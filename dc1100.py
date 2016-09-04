#!/usr/bin/env python

import socket
import time
import serial

CARBON_SERVER = '0.0.0.0'
CARBON_PORT = 2003


ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

line=""
while True:
    c = ser.read()
    if c != "\r" and c != "\n":
        line=line+c
    elif c == "\r":
        vals=line.split(",")
        sock = socket.socket()
        sock.connect((CARBON_SERVER, CARBON_PORT))
        sock.sendall('workshop.dc1100.val0 {} {}\n'.format(vals[0], int(time.time())))
        sock.sendall('workshop.dc1100.val1 {} {}\n'.format(vals[1], int(time.time())))
        sock.close()
        line=""


ser.close()
