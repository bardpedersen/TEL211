#!/bin/bash

#Task 1

read -p "Wich file with (directory) do you want to read" dir

if [ $# != 1 ]; then
    echo "You need to pass in one argument, no more or less."
    exit
fi


characters=3
words=0
lines=0
echo "The file testfile.txt contains ""$characters"" characters, ""$words"" words and ""$lines"" lines"