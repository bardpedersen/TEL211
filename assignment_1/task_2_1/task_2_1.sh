#!/bin/bash

#Task 1
number=0
for i in $@; do
    echo "$i""$number"
    number=$(( "$number"+5 ))
done