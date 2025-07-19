a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}

intersection = a & b
print("ผลร่วม (Intersection):", intersection)

difference = a - b
print("ผลต่าง (Difference a - b):", difference)

union = a | b
print("ผลรวม (Union):", union)

sym_diff = a ^ b
print("ค่าที่ไม่ซ้ำกัน (Symmetric Difference):", sym_diff)
