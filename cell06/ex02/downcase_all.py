#!/usr/bin/env python3
import sys
def downcase_it(string):
    return string.lower()
arg = sys.argv[1:]
if not arg:
    print("none")
else:
    for i in arg:
        print(downcase_it(i))
