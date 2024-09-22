#!/bin/bash

echo "Enter two numbers:"
read a b

# Swap the values
temp=$a
a=$b
b=$temp

echo "After swapping:"
echo $a $b
