#!/bin/bash

#Task 1
sudo apt show kapman

while true; do
    read -p "Do you wish to install this program? [Y/N]" yn
    case $yn in
        [Yy]* ) sudo apt install kapman; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

while true; do
    read -p "Do you wish to uninstall this program? [Y/N]" yn
    case $yn in
        [Yy]* ) sudo apt remove kapman; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
