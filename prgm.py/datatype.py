# 1.list
# fruits = ["apple", "banana", "mango"]
# print(fruits[1])  # banana
# fruits.append("orange")
# print(fruits)


# 2. tuple
# colors = ("red", "green", "blue")
# print(colors[0])  # red

# 3. Set
# numbers = {1, 2, 3, 3}
# print(numbers)  # {1, 2, 3}
# ➡ Automatically removes duplicates and is unordered.

# 4. Dictionary
# person = {"name": "Akshith", "age": 21, "country": "India"}
# print(person["name"])

# ➡ Stores data in key-value pairs for fast lookup.


# 5. Range
# for i in range(1, 6):
#     print(i)

# ➡ Useful for generating a sequence of numbers in loops.

# **primitive data types**
# 1. Integer (int)
# x = 25
# print(type(x))  # <class 'int'>

# ➡ Used for mathematical operations, counting, etc.

# 2. Float (float)
# y = 12.75
# print(type(y))  # <class 'float'>

# ➡ Used when precision (decimals) is required, like in financial or scientific calculations.

# 3. Complex (complex)
# z = 2 + 3j
# print(type(z))  # <class 'complex'>
# print(z.real, z.imag)  # Access real and imaginary parts

# ➡ Used in advanced mathematics and engineering.


# 4. Boolean (bool)
# is_valid = True
# print(type(is_valid))  # <class 'bool'>

# ➡ Used in conditions (if, while) to represent logical decisions.

# 5. String (str)
# name = "Akshith"
# print(type(name))  # <class 'str'>
# print(name.upper())  # String methods, #AKSHITH

# ➡ Used for text, words, or sentences. Strings are immutable.


# 6. NoneType
# data = None
# print(type(data))  # <class 'NoneType'>

# ➡ Represents the absence of value (used often to reset variables or as placeholders).

# time claculation for print
# import time
# s=time.perf_counter()
# n=3
# for i in range (n):
#     print(i)
# e=time.perf_counter()
# f=e-s
# print(f)

# s=time.perf_counter()
# n=3
# while i>n :
#     print(i)
# e=time.perf_counter()
# t=e-s
# print(t)
# if f>t:
#     print("false is more time")
# else:
# #     print("true is more time")
# # 

# # unpacking elements
# b=[1, 2, 3, 4, 5, 6, 7, 8, 8]
# a, *c, b, d=b
# print('a',a)
# print('c',c) 
# print('b',b)
# print('d',d)


import time
l=[1,2,3,3,4,4]
for i in l:
    print(i,'do work')
    print('wait for some time,,,,,,,,,!')
    time.sleep(3)
    print('you can go now......')
print('work is completed')



