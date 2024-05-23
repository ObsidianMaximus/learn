#!/bin/bash

read -p "Enter value of num" num

[[ $num -le 10 ]] && echo "Less than 10" || echo "Greater than 10" 
