#!/usr/bin/env python3
import sys 
if len(sys.argv) != 3: #ที่ต้องเป็น3 เพราะตัว1-->ชื่อไฟล์ , ตัวที่2--> ตัวแปรที่ส่งมาตัวเเรก , ตัวที่3--> ตัวแปรที่ส่งมาตัวสอง
    print("none")
else:
    userkey_input = sys.argv[1]
    userword_input = sys.argv[2]
    count_userkey = userword_input.count(userkey_input)
    if count_userkey > 0:
        print(count_userkey)
    else:
        print('None')