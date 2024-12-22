# print (list ())

# even = '246810'

# print (list (even))

# even1 = ('2','4','6','8','10')

# print (list (even1))

# even2 = ['2','4','6','8','10']

# print (list (even2))

# x = lambda a, b : (a+b)**2

# print(x(3,4))

# x = 0

# def increment():
#     global x
#     x=4
#     x+=1
#     print("lobal x",x)
    
# print("global x",x)

# increment()

# print("Now value of X",x)

# import os

# CONFIG_PATH = os.getenv("CONFIG_PATH", "/default/path")
# print(f"Package initialized with CONFIG_PATH: {CONFIG_PATH}")
# a = [1, 2, 3]  # Reference count = 1
# b = a           # Reference count = 2 (b references the same object)
# del a           # Reference count = 1 (a is deleted)

# #print(a)
# print(b)
# import gc
# class Node:
#     def __init__(self):
#         self.ref = None

# a = Node()
# b = Node()
# a.ref = b
# b.ref = a

# del a
# del b

# # gc.collect()
# import sys
# a = [1, 2, 3]
# print(sys.getrefcount(a))  # Outputs the reference count (additional count from the function call itself)

# arr = [i*i for i in range(4)]
# print(arr)

# s = 'abc'
# print(s[0:2])

# s +="def"

# print(s)

# myMap = {}
# myMap["alice"] = 88
# myMap["bob"] = 77

# print(myMap)

def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    s1 = set(str1)
    s2 = set(str2)
    
    common = s1 & s2
    
    print("Common characters in both strings are: ", common)

common_letters()