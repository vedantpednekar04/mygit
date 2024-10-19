#9) display fibonicii series of 10 numbers
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Display the first 10 Fibonacci numbers
fib_10 = fibonacci(10)
print(fib_10)
