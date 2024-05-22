#!/usr/bin/env python3
import socket
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ManageData import DecryptData
from config import serverMACAddress, wheelSensitivity, pedalsSensitivity, port
try:

    print('starting ev3dev')
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C) # creates motor pair
    print('ev3dev ready')
    print('starting server')
    # connects to server
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect((serverMACAddress,port))
    print('client ready')
    while True:
        #gets data
        data = DecryptData(client.recv(1024))
        # checks for quit
        if str(data[0]) == "q":
            client.send(str(False).encode('utf-8'))
            break # stops program when reciving q
        else:
            if abs(data[0]) > 0.1 or data[0]: # dead zone
                steering = data[0] * wheelSensitivity
            else: steering = 0
            if abs(data[1]) > 0.1: # dead zone
                speed = data[1] * pedalsSensitivity
                motor_pair.on(steering,speed)
            else:
                motor_pair.off() # disables motor if no speed
                speed = 0
            
            client.send(str(True).encode('utf-8')) # notifys the server that everything is fine
            
except Exception as e:
    print('error!:',e) # errors are not fun
    
finally:
    client.close() # kills client

