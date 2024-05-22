# EV3SteeringWheel
 welcome this is an app designed to allow you to control an ev3 robot running ev3dev using a steering wheel
## Step 1:
 make sure your steering wheel is compatible
 go to https://hardwaretester.com/gamepad
 1. is your wheel recognized? if its not then check drivers and pc compaitblity
 2. can you see the wheels rotaithon in one of the axis?
 3. are the pedals combined into one axis? if it isnt check your settings for an opithon to enable it
## Step 2:
 downlod all the code on here to your pc,
 run configCreator.py and follow the instrucithons
## Step 3:
 connect your [ev3 to bluetooth](https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth)
 then download ManageData.py, client.py, config.py to your ev3
 then run server.py wait for it to say "server ready"
 then run client.py on ev3

 ## common issues:
 im using pygame for inputs becuse its the best thing i could find
 but its made for games, so i made a 1x1 display and you have to have it be the active window
 inorder for the program to read your steering wheel
