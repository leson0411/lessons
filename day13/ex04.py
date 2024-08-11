def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

"""
n = 60
ab = n
a <= b
a^2 <= ab = n
a <= sqrt(n)
2 30
3 20
4 15
5 12
6 10
"""


print(is_prime(15))
