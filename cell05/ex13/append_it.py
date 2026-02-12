#!/usr/bin/env python3
import sys
arg = sys.argv[1:] 
if len(arg) == 0:
    print("none")
else:
    found = False
    for word in arg:
        if not word.endswith("ism"): # ใช้matchingตรวจว่าลงท้ายด้วยismมั้ย
            print(word + "ism")
            found = True
    if not found: # ถ้าทุกคำลงท้ายด้วย ism หมดก็print none
        print("none")
