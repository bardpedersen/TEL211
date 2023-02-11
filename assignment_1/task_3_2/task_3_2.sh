#!/bin/bash

#Task 1
git clone https://github.com/NMBURobotics/bash_basic_examples.git

cd bash_basic_examples
cd scripts

for f in *.sh; do
  bash "$f" 
done
