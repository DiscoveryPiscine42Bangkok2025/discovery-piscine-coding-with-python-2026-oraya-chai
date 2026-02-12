#!/usr/bin/env python3
import sys
if len(sys.argv) != 1: # ถ้ามี argument มากกว่า 1 ตัว (ชื่อไฟล์ + อย่างอื่น)
    print("none")
else:
    table = 0
    while table <= 10:
        print(f"Table de {table}:", end="") # ระบุว่าไม่ต้องขึ้นบรรทัดใหม่

        i = 0
        while i <= 10:
            print(f" {table * i}", end="")
            i += 1

        print() # ให้ขึ้นบรรทัดใหม่
        table += 1
