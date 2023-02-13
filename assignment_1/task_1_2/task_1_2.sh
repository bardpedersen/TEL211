#!/bin/bash

#Task 1
document_value_1="magician who have lost their magic?"

#Task 2
document_value_2="Ian"

#Task 3
picture_data="P1\n-# A very tiny picture\n-6 10\n-1 0 0 0 0 1\n-0 0 0 0 0 0\n-0 1 0 0 1 0\n-0 0 0 0 0 0\n-0 0 1 1 0 0\n-0 0 0 0 0 0\n-0 1 0 0 1 0\n-0 1 1 1 1 0\n-0 0 0 0 0 0\n-1 0 0 0 0 1"

#Task 4 
if [ $# != 1 ]; then
    echo "You need to pass in one argument, no more or less."
    exit
fi

#Task 5
user="$1"

#Task 6
mkdir -p "$user""_directory"/{"$user""_documents","$user""_music","$user""_pictures"}

#Task 7
tar -xf some_files.tar.gz

#Task 8
cp some_files/*.txt "$user""_directory"/"$user""_documents"
cp some_files/*.wav "$user""_directory"/"$user""_music"
cp some_files/*.png "$user""_directory"/"$user""_pictures"

#Task 9
cat "$user""_directory"/"$user""_documents"/*.txt

#Task 10
echo "$document_value_1" > "$user""_directory"/"$user""_documents"/a_very_important_file.txt

#Task 11
echo "$document_value_2" >> "$user""_directory"/"$user""_documents"/a_very_important_file.txt

#Task 12 
cat "$user""_directory"/"$user""_documents"/a_very_important_file.txt

#Task 13
echo "$picture_data" > "$user""_directory"/"$user""_pictures"/a_very_tiny_picture.pgm

#Task 14
date=$(date '+%y%m%d_%H%M%S')
tar -cJf "$user""_directory_""$date.tar.xz" "$user""_directory"
