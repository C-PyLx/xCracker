#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#Uninstall the xCracker script !
#If you uninstall xCracker\
#You can't use them anywhere!
#----------------------------
#Thanks for using xCracker :)
#Follow me on github:
#https://github.com/C-PyLx
#Report bugs to:
#https://t.me/Ac3ess

green='\e[0;32m'
red='\e[0;31m'
cyan='\e[0;96m'
end='\e[0;37m'

clear

echo -e $red"""                ___            _        _ _
|-|   |-| _ __ |_ _|_ __  ____| |_ __ _| | |
|-|   |-|| ._ \ | || ._ \/  __| __/ _. | | |
|-|___|-|| | | || || | | \__  \ || (_| | | |
|___-___||_| |_|___|_| |_|____/\__\__._|_|_| .....
"""$end

echo -e $red"[ ! ] UnInstalling 'xCracker' ..."$end
echo -e $cyan"[ ! ] This may take a moment :)"$end
echo

rm /opt/xCracker/*
rmdir /opt/xCracker

rm /usr/bin/xCracker
rm /usr/bin/xCracker-install
rm /usr/bin/xCracker-uninstall

sleep 1

echo

echo -e $green"[ ✔ ] 'xCracker' Uninstalled successfully."$end
echo -e $green"[ + ] Thanks for using 'xCracker' :)"$end
echo
echo -e $cyan"[ + ] Follow me on github: https://github.com/C-PyLx"$end
echo -e $cyan"[ + ] Report bugs to: https://t.me/Ac3ess"$end
echo