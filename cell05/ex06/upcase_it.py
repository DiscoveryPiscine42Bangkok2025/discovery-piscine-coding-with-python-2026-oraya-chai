#!/usr/bin/env python3
import sys # นำเข้า module sys ใช้เพื่อเข้าถึง sys.argv (ข้อมูล parameter ที่ส่งมาจาก command line)
if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())

# sys.argv คือ list ของค่าที่พิมพ์ตามหลังชื่อโปรแกรม
# len(sys.argv) ต้องเป็น 2 เท่านั้นถึงจะถูก = ชื่อไฟล์, string ที่ผู้ใช้ส่งมา

