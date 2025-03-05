#!/bin/bash

read -p "Please enter Python file name: " name

python3 $name < input01.txt > output.txt

# python3 $name < input01.txt > expected01.txt

# echo "hi"
# echo "hi" > expected02.txt