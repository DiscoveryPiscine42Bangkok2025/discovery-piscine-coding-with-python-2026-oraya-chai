#!/usr/bin/env python3
import sys
if len(sys.argv) != 3: # ตรวจสอบจำนวน parameter ต้องมี3อัน ชื่อไฟล์ เลข1 เลข2
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        numbers = list(range(start, end + 1)) # range ปกติไม่รวม end ต้อง +1
        print(numbers)
    except ValueError:
        print("none")
# ใช้ try except กันไว้เผื่อเกิดerrorตอนแปลงค่าเป็น int