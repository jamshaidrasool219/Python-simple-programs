# Program: Functions ki examples
def greet(name):
    return f"Hello, {name}!"


def square(n):
    return n * n


def is_even(n):
    return n % 2 == 0


def power(base, exp=2):
    return base ** exp


print(greet("Jamshaid"))
print("Square of 5:", square(5))
print("8 even hai?", is_even(8))
print("2^10 =", power(2, 10))
print("Default power (3^2) =", power(3))
