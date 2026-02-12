#!/usr/bin/env python3
old_arrays = [2, 8, 9, 48, 8, 22, -12, 2]
# กรองเอาเฉพาะตัวที่ > 5 แล้วค่อยบวก 2
new_arrays = [x + 2 for x in old_arrays if x > 5]
print(old_arrays)
print(new_arrays)