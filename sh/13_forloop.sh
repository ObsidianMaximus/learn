#!/bin/bash

#First method
for i in 1 2 3 4 5
do
	echo "Number is $i"
done

#Second method
for i in {1..20}
do
	echo "Haha $i"
done

#Third method
for i in "Hello" "Guys" "Welcome" "Back"
do
	echo "$i"
done

#For loop with files

i="/home/obsidian/Documents/software"
for i in $(cat $i)
do
	echo $i
done
