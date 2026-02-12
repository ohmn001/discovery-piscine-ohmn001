#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit() 

input_string = sys.argv[1]
result = ""

#เช็คตัวอักษร 'z' 
for char in input_string:
    if char == 'z':
        result = result + 'z'

#ตรวจสอบผล
if result == "":
    print("none")
else:
    print(result)