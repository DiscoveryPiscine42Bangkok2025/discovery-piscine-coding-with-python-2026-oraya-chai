#!/usr/bin/env python3
def add_one(num):
    num += 1
    print(f"call the method: {num}")

num1 = 5
print(f"without call the method: {num1}")

add_one(num1)

print(f"after call the method: {num1}") # ค่าของnum1ไม่เปลี่ยนหลังเรียกฟังก์ชัน