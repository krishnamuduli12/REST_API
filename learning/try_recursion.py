def tri_recursion(k):
    if k> 0:
        print('value of ke before calling fun: ', k)
        result = k + tri_recursion(k-1)
        print('value of ke after calling fun: ', k)
        print(result)
    else:
        result = 0
    return result

print('\n\n Recusion Example Results')
tri_recursion(6)