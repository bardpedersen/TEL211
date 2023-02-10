#!/bin/bash

#Task 1
random_nr=$(( RANDOM % 10))
num_a=100

while [ "$num_a" != "$random_nr" ]; do
    echo "Enter guess between 0 and 10"
    read -r num_a

    if [ "$num_a" -lt "$random_nr" ]; then
        echo "The number is higher"
    elif [ "$num_a" -gt "$random_nr" ]; then
        echo "The number is lower"
    else 
        echo "You guessed right, the number was ""$random_nr"
    fi
done
