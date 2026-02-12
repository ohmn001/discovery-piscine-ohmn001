#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    
for arg in sys.argv[1:]:
    # .endwith --> เช็คว่าคำนั้นไม่ได้ลงท้ายด้วย "ism"
    if not arg.endswith("ism"):
        print(arg + "ism")