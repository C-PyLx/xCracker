#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#----------------------
#xCracker installer
#Install it & use them enywhere
#Follow me on github:
#https://github.com/C-PyLx
#Report bugs:
#https://t.me/Ac3ess

clear

green='\e[0;32m'
red='\e[0;31m'
cyan='\e[0;36m'
end='\e[0;37m'

echo -e $red""" ___           _        _ _
|_ _|_ __  ___| |_ __ _| | |
 | || ._ \/ __| __/ _. | | |
 | || | | \__ \ || (_| | | |
|___|_| |_|___/\__\__._|_|_| .....
"""$end

echo -e $green"[ + ] Installing xCracker ..."$end
echo -e $cyan"[ + ] Please wait, Just a moment."$end

mkdir /opt/xCracker

echo "[ - ] Please enter root password to install [if you have password!]:"

sudo chmod +x install.sh
sudo chmod +x uninstall.sh
sudo chmod +x xCracker.py

cp version.txt /opt/xCracker
cp Readme.txt /opt/xCracker
cp words.txt /opt/xCracker
cp hash.txt /opt/xCracker

cp install.sh /usr/bin/xCracker-install
cp uninstall.sh /usr/bin/xCracker-uninstall
cp xCracker.py /usr/bin/xCracker
cp words.txt /usr/bin

sleep 1

echo
echo -e $green"[ ✔ ] xCracker installed successfully."$end
echo
echo -e $cyan"[ + ] Use xCracker with command: xCracker.py -h, --help for help usage!"$end
echo -e $cyan"[ + ] Remove xCracker with command: xCracker-uninstall !"$end
echo

echo -e $green"\t[ - ] Do you want to start xCracker? [Y]es, [N]o: "$end

read start

if [[ $start == "Y" || $start == "y" ]]; then
	xCracker --help
else
	clear
fi
