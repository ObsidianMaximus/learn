#!/bin/bash

# We will be making Key-Value pairs here in arrays.


declare -A array

array=([name]="max" [surname]="hello guys!" [city]="Mumbai")

echo "The values of name key is ${array[name]}"
echo "The value of all keys is ${array[*]}"
