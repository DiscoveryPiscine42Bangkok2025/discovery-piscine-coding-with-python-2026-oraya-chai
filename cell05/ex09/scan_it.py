#!/usr/bin/env python3
import sys
import re
if len(sys.argv) != 3: # ชื่อไฟล์ + 2 params
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    find = re.findall(keyword, text) # เก็บเป็น list
    if len(find) == 0:
        print("none")
    else:
        print(len(find))