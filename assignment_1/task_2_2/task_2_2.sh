#!/bin/bash

#Task 1
Calculate_volum() {	

    if [ $# != 3 ]; then
        echo "You need to pass in three argument: height, width, length."
        exit
    fi
    number=$(( "$1"*"$2"*"$3" ))
    echo "The volume of the cube is ""$number"

}

Calculate_volum 10 5 1