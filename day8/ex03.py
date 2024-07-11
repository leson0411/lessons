for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        print(dividend, end=" ")
