def Cube(n):
    return n*n*n

num = (1,2,3,4)

result = map(Cube, num)
print(result)

# Converting map object to a list
cube_list = list(result)
print('List of Cubes:', cube_list)

def Fullname(FN, LN):
    return FN+ "_" +LN

FN = ('John', 'Sam', 'Jean')
LN = ('Smith', 'Rodgrigues', 'paul')

result = map(Fullname, FN, LN)

print(result)
print(list(result))