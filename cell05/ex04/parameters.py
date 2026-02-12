#!/usr/bin/env python3

import sys #method python ที่ใช้เกี่ยวกับ ข้อมูลที่ใส่เข้ามาผ่าน terminal
#sys.argv สมาชิกตัวแปรที่ input ผ่าน terminal มาในยบรรทัดนั้น
# len - 1 เพราะว่า ใน terminal จะมอง ./parameter.py(ชื่อไฟล์) เป็นตัวที่1
print(f"Number of parameters: {len(sys.argv) - 1}") 