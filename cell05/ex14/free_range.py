#!/usr/bin/env python3
import sys
# ตรวจสอบว่าพารามิเตอร์ที่ส่งมามีครบ 2 ตัวหรือไม่ (sys.argv[0] คือชื่อไฟล์)
if len(sys.argv) != 3:
    print("none")
    sys.exit()

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # ถ้าเลขแรกน้อยกว่าเลขหลัง จะเรียงขึ้น ถ้ามากกว่าจะเรียงลง
    if start <= end :
        step = 1 
    else :
        step = -1
    result = list(range(start, end + step, step))

    print(result)

except ValueError:
    print("none")