a = [1, 2, 3]
b = [1, 2, 3]

print(id(a), id(b))
print(a is b)  # False
print(a == b)  # True

c = a

print(id(a) == id(c))  # True

print(a is c)  # True
print(a == c)  # True
