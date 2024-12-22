# def greet(name):
#     return f"hello, {name} !!!"

# say_hello = greet
# print(say_hello("krish"))

# def execute_fun(fun, value):
#     return fun(value)

# print(execute_fun(fun,"bob"))

def multiplier(factor):
    def multiply_by(x): 
        return x*factor
    return multiply_by
double = multiplier(2)
print(double(5))
