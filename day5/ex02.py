numbers = [1, 2, 3, 4]
print(id(numbers))

numbers = numbers + [5]
print(id(numbers))

numbers = [1, 2, 3, 4]
print(id(numbers))

numbers.remove(4)
print(id(numbers))

# print(id(numbers) == id(new_numbers))
# print(numbers is new_numbers)
