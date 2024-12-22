# one value is False, others are True
list2 = [0, 1, 2, 3]
print(all(list2))

list1 = ['Hey', 'Hello', 'Python', 'Program']
print(all(list1))

# all values are False
list3 = [0, False]
print(all(list3))

# empty list
list4 = []
print(all(list4))