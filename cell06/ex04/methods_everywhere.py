#!/usr/bin/env python3
import sys
def shrink(string):
    print(string[:8]) # แสดง8ตัวแรกของstring
def enlarge(string):
    while len(string) < 8:
        string += 'Z'
    print(string)

arg = sys.argv[1:] # เอาชื่อfileออก
if len(arg) < 1:
    print("none")
else:
    for i in arg:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)
