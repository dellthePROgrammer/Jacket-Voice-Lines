#!/bin/bash

# Bash file that will install all the needed modules to run the file
sudo apt update
sudo apt install python3 idle3 pip3 rpi.gpio libsdl2-dev
pip3 install -y pygame
echo If you wish to upgrade the system type "sudo apt upgrade -y"