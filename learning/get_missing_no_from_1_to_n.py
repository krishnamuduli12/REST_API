#Thre is a range of number from 1 to n but in between one no is missing
def get_missing_summation(a):
    n = a[-1]
    sum1 = 0
    total = n*(n+1)/2
    
    sum1 = sum(a)
    print(int(total - sum1))
 
 
def get_missing_xor(a):
    n = len(a) 
    xor_a = a[0]
    for index in range(1,n):
        xor_a = xor_a^a[index]
    x2 = 0
    for j in range(1, n+2):
        x2 = x2^j
        
    print(xor_a^x2)

a = [1,2,3,4,6,7,8,9]
get_missing_summation(a)
get_missing_xor(a)
