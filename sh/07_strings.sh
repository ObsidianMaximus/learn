#!/bin/bash

name="Your name is haha"

len_name=${#name}

#Finding the length
echo "Name is $name and it's length is $len_name"

#Upper and lower case
echo "The upper case is ${name^^} and the lower case is ${name,,}"

#Replacing the whole string
echo "Replacing name: $name with age: ${name/*/14}"

#Replacing only a single word in the string
echo "Replacing name: $name with new name: ${name/haha/max}"

#Slicing a string
echo "Slicing it: ${name:5:4}"
