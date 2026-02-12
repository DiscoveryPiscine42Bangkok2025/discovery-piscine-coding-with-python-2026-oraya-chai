#!/usr/bin/env python3
import sys
count = len(sys.argv) - 1 # sys.argv คือ list ของ parameter ทั้งหมด ลบหนึ่งเพราะไม่นับชื่อไฟล์
print(f"Number of parameters: {count}.")