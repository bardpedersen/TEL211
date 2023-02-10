#!/bin/bash

#Task 1
user="linus_torvalds"

#Task 2
mkdir "$user"

#Task 3
user2="_2"
cp -R "$user" "$user$user2"

#Task 4
cd "$user$user2"

#Task 5
touch "file_1"
touch "file_a"
touch "dangervirus"

#Task 6
ls

#Task 7
ls|grep "file"

#Task 8
mv dangervirus .dangervirus

#Task 9
ls

#Task 10
ls -a 

#Task 11
echo "Have a nive day" "$user"