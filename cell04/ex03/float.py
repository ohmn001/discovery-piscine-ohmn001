#!/usr/bin/env python3

user_input = input('Give me a number: ') #input จะได้ data type เป็น str

try:
    number = float(user_input)

    if number.is_integer():
    #if number == int  ใช้ไม่ได้เพราะ มันไม่สามารถเปรียบเทียบกับตัวแปรตรงๆได้ อีกอย่าง เราแปลงให้ input เป็น float เเล้วยังไงมันก็เข้า else 
        print('This number is an integer.')
    else:
        print('This number is a decimal.')

except ValueError:
    print('Please enter a valid number.')