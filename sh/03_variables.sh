#!/bin/sh

#This script is for variables testing.

haha="hello guys!"
hoster=$(hostname)

echo "Print $haha, my hostname is: $hoster"

haha="overwritten"

echo "haha is $haha"
