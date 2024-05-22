from socket import socket, AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM
from keyboard import is_pressed
from ManageData import EncryptData
from config import serverMACAddress, port
import pygame
s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)
pygame.init()
try:
    #creates server
    print('server starting up') 
    backlog = 1
    size = 1024
    # connects server
    s.bind((serverMACAddress, port))
    s.listen(backlog)
    print('server ready')
    #finds client
    clientSocket, clientAddress = s.accept()
    print(f'new ev3[{clientAddress}]')
    run = True
    while run:
        if is_pressed('q'): # press q to stop program
            clientSocket.send(EncryptData(f'q 0'))
            break
        #creates pygame joystick
        joy = pygame.joystick.Joystick(0)
        #manages events
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
        # gets wheel and pedals data
        wheel, pedals = joy.get_axis(0),joy.get_axis(3)
        data = f'{wheel} {pedals}'
        clientSocket.send(EncryptData(data))
        status = bool(clientSocket.recv(1024))
        if not status: # leaves
            print(f'ev3[{clientAddress}] has left!')
            clientSocket.close()
            break

except Exception as error:
    print(f'error!\n {error}') # prints error
finally:
    s.close() # closes server
