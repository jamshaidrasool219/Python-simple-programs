# Program: Recursion ki examples
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)


print("5! =", factorial(5))
print("Fibonacci(7) =", fibonacci(7))
print("1 se 10 tak sum =", sum_to_n(10))
