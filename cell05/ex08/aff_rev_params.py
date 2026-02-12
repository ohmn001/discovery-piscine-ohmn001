#!/usr/bin/env python3

user_input = input()
args = user_input.split() #ใน() มองเป็นช่องว่าง ก็คือ เเบ่งคำตามช่องให้เป็น List

if len(args) < 2:
    print("none")
else:
    for word in args[::-1]: #args[::-1] ต่างจาก range(n,m)
        print(word)