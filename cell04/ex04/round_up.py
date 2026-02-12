#!/usr/bin/env python3

num_input = float(input("Give me a number: "))


if num_input == int(num_input):
    result = int(num_input)
else:
    result = int(num_input) + 1

print(result)