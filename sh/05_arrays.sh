#!/bin/sh

#Arrays are space seperated values

myArray=("haha" 1 3 5)

echo "All the values in the array are: ${myArray[*]}"
echo "${myArray[3]}"

#Finding the length of an Arrays


echo "Length of the array is : ${#myArray[*]}"


#Truncating the array

echo "Values from index 2 and only 1 value is ${myArray[*]:2:1}"

#Updating the array

myArray+=("Val1" "Val2")

echo "Updated array elements are: ${myArray[*]}"
