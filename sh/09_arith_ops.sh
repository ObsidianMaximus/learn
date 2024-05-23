#!/bin/bash

#Script for arithmetic operations.

#Using 'let' keyword
let num=2+2

echo "$num"

let num++

echo "$num"

#Using double parenthesis '(())'
echo "$((num*9))"
