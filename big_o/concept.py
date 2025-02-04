
#O(1) - Constant Time:
#ในกรณีนี้ เราสามารถใช้ฟังก์ชันที่มีเวลาการทำงานคงที่ไม่ว่าขนาดของข้อมูลจะเป็นเท่าไหร่ก็ตาม
# def constant_example(items):
#     return items[0]

# # เรียกใช้ฟังก์ชัน
# items = [1, 2, 3, 4, 5]
# print(constant_example(items))  # ผลลัพธ์: 1




#O(n) - Linear Time:
#ในกรณีนมีการทำงานที่มีความเชื่อมโยงกับขนาดของข้อมูล
# def linear_example(items):
#     for item in items:
#         print(item)

# # เรียกใช้ฟังก์ชัน
# items = [1, 2, 3, 4, 5]
# linear_example(items)  # ผลลัพธ์: 1 2 3 4 5


# O(n^2) - Quadratic Time:
# ในกรณีนี้ เรามีการทำงานที่เพิ่มขึ้นเป็นสี่เท่าเมื่อขนาดข้อมูลเพิ่มขึ้นเป็นสองเท่า
# def quadratic_example(items):
#     for item1 in items:
#         for item2 in items:
#             print(item1, item2)

# # เรียกใช้ฟังก์ชัน
# items = [1, 2, 3]
# quadratic_example(items)  


# O(n^2) - Quadratic Time:
# ในกรณีนี้ เรามีการทำงานที่เพิ่มขึ้นเป็นสี่เท่าเมื่อขนาดข้อมูลเพิ่มขึ้นเป็นสองเท่า
# python
# def quadratic_example(items):
#     for item1 in items:
#         for item2 in items:
#             print(item1, item2)

# # เรียกใช้ฟังก์ชัน
# items = [1, 2, 3]
# quadratic_example(items)  




# O(log n) - Logarithmic Time:
# ในกรณีนี้ เรามีการลดขนาดข้อมูลอย่างมีประสิทธิภาพตามฟังก์ชันล็อก

# import math

# def log_example(n):
#     return math.log(n)

# # เรียกใช้ฟังก์ชัน
# print(log_example(100))  # ผลลัพธ์: 4.605170185988092




# O(n log n) - Linearithmic Time:
# ในกรณีนี้ เรามีการทำงานที่มีประสิทธิภาพเสมอเมื่อขนาดข้อมูลเพิ่มขึ้น แต่ไม่ใช่อย่างเชื่อมโยงเช่นเดียวกับกรณี Quadratic

# def n_log_n_example(items):
#     items.sort()  # เรียงลำดับข้อมูล
#     for item in items:
#         print(item)

# # เรียกใช้ฟังก์ชัน
# items = [3, 1, 4, 2, 5]
# n_log_n_example(items)  # ผลลัพธ์: 1 2 3 4 5
