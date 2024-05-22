import pygame
from keyboard import is_pressed
from time import sleep
root = pygame.display.set_mode((1,1))
run = True
pygame.init()
wheel_axis_id = 0
pedal_axis_id = 0
axisFindingStatus = 0
joy = pygame.joystick.Joystick(0)
print('STEP ONE')
print(f'you will be given the info coming from {joy.get_numaxes} press any button to skip axis 1 to mark as wheel 2 to mark as pedals')
print('also make sure to have the 1x1 pygame window that will open active')
print('press enter to continue')
while not is_pressed('return'): pass
for i in range(joy.get_numaxes()):
        sleep(0.1)
        axis = joy.get_axis(i)
        innerRun = True
        if axisFindingStatus >= 2: break
        while innerRun:
                joy = pygame.joystick.Joystick(0)
                print(joy.get_axis(i))
                if is_pressed('1'):
                    wheel_axis_id = i
                    axisFindingStatus+=1
                    innerRun = False
                elif is_pressed('2'):
                    pedal_axis_id = i
                    axisFindingStatus+=1
                    innerRun = False
                elif is_pressed('return'):
                    innerRun = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
print('STEP 2')
print('wheel Sensitvity goes from 100 to 0, 100 meaning you can do a 360, 0 meaning you cant steer')
wheelSensitivty = input('ENTER WHEEL SENSITVITY: ')
print('pedal Sensitvity goes from 100 to 0, 100 meaning you can go max  speed, 0 meaning you cant move')
pedalSensitivty = input('ENTER PEDAL SENSITVITY: ')
print('STEP 3')
print('the following step changes according to your os')
userOS = input('what is your os (windows, linux, mac): ')
if userOS == 'windows':
    print('open device manager')
    print('go to bluetooth and find your adapter, it will have a company that makes adapters name something like intel wireless bluetooth')
    print('then rightclick properties then advanced')
    bluetoothAddress = input('you will see a address something like 70:cd:0d:c5:93:d2 please enter it\n')
elif userOS == 'linux':
    print('open terminal')
    print(' run the "hciconfig" command')
    print('look for hci0 or similar')
    bluetoothAddress = input('a bluetooth address will be listed next to "BD Address" please enter it\n')
elif userOS == 'mac':
    print('i dont have a mac so i cant help you :(')
    print('look online on how to get your blueTooth adapter address')
    bluetoothAddress = input('if you succeded then enter it here:\n')
else: print('ERROR OS NOT FOUND')
finalConfig = f'wheelSensitivity = {wheelSensitivty} # the sensitivity of the wheel maximum 100 for up to 360 turn\npedalsSensitivity = {pedalSensitivty} # the sensitivity of the pedals maximum 100 for up to max speed\nport = {4} # the port of the server\nserverMACAddress = "{bluetoothAddress}" # the Address the server will run on'
config = open('config.py', 'w')
config.write(finalConfig)
config.close()
print('notes: if you have any issues try changing the port in config.py')
print('you can change the settings manuly in config.py')
print('now your ready! simply connect the ev3 to your comptuer with bluetooth\ndownload the config.py ManageData.py and client.py to your ev3\nand run server.py on your computer once it says "server ready" start the client.py on the ev3')