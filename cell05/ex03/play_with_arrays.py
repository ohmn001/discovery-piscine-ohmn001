#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]


unique_values = set(original_array) # set จะตัดตัวที่ซ้ำกันทิ้งให้เราโดยอัตโนมัติ #data type ของมันจะกลายเป็น set เลย
New_array = [n for n in unique_values] #ลูปแปลงกลับให้เป็น list เบบในโจทย์
print(original_array)      
print(New_array )     