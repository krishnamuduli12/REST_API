# Python program to illustrate print()
# Passing sep and end parameters
num = 7
print('James Bond ', num, sep = '--> 00', end = '\n\n\n')

a = 2
print('Value of a: ', a, sep = '000', end = '\n')

print('Computer', 'Downloads', 'Wallpapers', 'Img1.png', sep = '/')

myfile = open('Student.txt', 'w')
print('This file contains student details', file = myfile)
myfile.close()