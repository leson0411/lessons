# Bài 1: Tính S(n) = 1 + 2 + 3 + … + n
"""
input: n (int, positive)
output: S(n)

n = 5
S = 1 + 2 + 3 + 4 + 5 = 15
range(1, n+1)
total = 0
S(5) = S(4) + 5 = 15
S(4) = S(3) + 4 = 10
S(3) = S(2) + 3 = 6
S(2) = S(1) + 2 = 3
S(1) = 1
"""
n = int(input('n = '))

# t = 0
#
# for x in range(1, n+1):
#     t = t + x
#
# print(t)

t = n*(n+1)//2
print(t)
