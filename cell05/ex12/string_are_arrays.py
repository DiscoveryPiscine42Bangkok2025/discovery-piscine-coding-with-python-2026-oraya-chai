#!/usr/bin/env python3
import sys
if len(sys.argv) != 2: # มี parameter แค่ 1 ตัวเท่านั้น -> ชื่อไฟล์
    print("none")
else:
    text = sys.argv[1]
    zcount = 0
    for i in text:
        if i == 'z':
            zcount += 1
    if zcount == 0:
        print("none")
    else:
        print("z" * zcount)
