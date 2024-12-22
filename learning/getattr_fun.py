class Employee:
    name='krishna'
    sal=223000
    designation='ciso'
    
e = Employee()

print('Salary of Krish is: ', getattr(e, 'sal'))
print('Salary of Krish is: ', e.sal)