#!/bin/bash

#Script for using if else conditional statement


read -p "Enter the zram ratio: " zram
if [[ $zram -gt 0 ]]; then
	echo "Your zram ratio to ram has been set to $zram"
else
	echo "Wrong ratio!"
fi

if [ $zram -le 3 ]
then
	echo "Set to 3"
elif [ $zram -le 6 ]
then
	echo "set to 6"
elif [ $zram -ge 10 ]; then
	
	echo "Greater than or equal to 10"
else
	echo "Wrong input!"
fi
