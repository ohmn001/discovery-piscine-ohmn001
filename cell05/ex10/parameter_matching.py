#!/usr/bin/env python3
import sys

# sys.argv[0] คือชื่อไฟล์, sys.argv[1] คือค่าที่ส่งมา
if len(sys.argv) != 2: #ที่ต้องเป็น2 เพราะตัว1-->ชื่อไฟล์ , ตัวที่2--> ตัวแปรที่ส่งมา
    print("none")
else:
    parameter = sys.argv[1]
    user_word = input("What was the parameter? ")
    if user_word == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")