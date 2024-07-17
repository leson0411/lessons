card_num = list(input("Enter the number of the card: ").strip())
checking_digit = card_num.pop()
card_num.reverse()

divide_digit = []

for index, num in enumerate(card_num):
    if index % 2 == 0:
        double_num = int(num) * 2
        if double_num > 9:
            double_num -= 9
        divide_digit.append(double_num)
    else:
        divide_digit.append(int(num))

total = sum(divide_digit) + int(checking_digit)

# if total % 10 == 0:
#     print("Valid!")
# else:
#     print("Invalid!")

print("Valid" if total % 10 == 0 else "Invalid")
