#!/bin/bash

#Task 1

if [ $# != 1 ]; then
    echo "You need to pass in one argument, no more or less."
    exit
fi

a=($(wc $@))
lines=${a[0]}
words=${a[1]}
characters=${a[2]}
name=${a[3]}

echo "The file ""$name"" contains ""$characters"" characters, ""$words"" words and ""$lines"" lines"