#!/bin/bash

read -p "Enter a number between 0 to 5" num

case $num in
	0) cal;;
	1)date;;
	2) 
		echo "Hello"
		echo "Bye"
		;;
	3) 	
		echo $PATH;;
	4)echo "Your name is $(hostname)";;
	5)sudo apt update && sudo apt upgrade -y;;
esac
