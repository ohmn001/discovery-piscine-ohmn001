#!/usr/bin/env python3

import sys

if len(sys.argv) == 2: 
    print(sys.argv[1].lower())
else:
    # ถ้าไม่มีพารามิเตอร์เลย หรือ มีมากกว่า 1
    print("none")