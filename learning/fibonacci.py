def generate_fibonacci(n):
    fib_series = [0,1]
    
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series

num_terms = int(input("Enter number of terms for fibonacci series: "))
fibonacci_series = generate_fibonacci(num_terms)
print("Fibonacci Series upto",num_terms,"terms:",fibonacci_series)