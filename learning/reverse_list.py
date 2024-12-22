#reverse a list
list1 = [2,4,6,7,9]
#list1.reverse()
# list2 =list(reversed(list1))
# print(list2)
#print(list1[::-1])

list3 =[]
for i in range(len(list1)-1,-1,-1):
    list3.append(list1[i])
print(list3)

