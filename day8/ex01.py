import random


num = random.randint(1, 100)

while True:
    guess = int(input("Enter a guess number: "))

    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("You guess correctly!")
        break

