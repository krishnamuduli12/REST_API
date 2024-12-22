def cube(c):
    return c*c*c

#using lambda function
# l_cube = lambda c: c*c*c

# print(cube(6))

# print(l_cube(7))

# li = [5,7,25,97,82,19,45,23,73,57]

# final_li = list(map(lambda x: x**2, li))
# print(final_li)

def new_func(x):
    return(lambda y: x+y)

t = new_func(5)
u = new_func(6)

print(t(7))
print(u(8))