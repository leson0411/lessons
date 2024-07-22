def add(num1, num2):
    total = num1 + num2
    return total


print(add(2, 3))


def subtract(a, b):
    return a - b


print(subtract(a=6, b=2))


def multiply(c, d):
    return c * d


print(multiply(7, 3))


def divide(m, n):
    if n == 0:
        print("Warning")
    else:
        return m / n


print(divide(9, 2))
