# a = []
#
# for i in range(5):
#     a.append(i**2)
#
# print(a)

# a = [i**2 for i in range(5)]
#
# print(a)

# a = []
#
# for i in range(3):
#     for j in range(4):
#         if j < 2:
#             a.append([i, j])
#
# print(a)

# a = [
#     [i, j]
#     for i in range(3)
#     for j in range(4)
#     if j < 2
# ]
#
# print(a)

# a = [
#     'a' if i < 3 else 'b'
#     for i in range(5)  # 0 1 2 3 4
# ]
#
# print(a)
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# a = [1, 3, 2]
# a.sort()
#
# print(a)

# records.sort(key=lambda x: (x[1], x[0]))
# new_list = sorted(records, key=lambda x: (x[1], x[0]))
#
# print(new_list)

a = [1, 3, 2, 1, -1]

# min_val = a[0]
#
# for x in a:
#     if min_val > x:
#         min_val = x
#
# print(min_val)

# min_val = min(a)
#
# print(min_val)

# lst = []
# scores = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     lst.append([name, score])
#     scores.append(score)
# lst.sort(key=lambda x: (x[1], x[0]))
#
# scores_no_mins = [x for x in scores if x != min(scores)]
#
# for name, score in lst:
#     if score == min(scores_no_mins):
#         print(name)

# a = [1, 2, 3]
# print(list(map(str, a)))  # element-wise

# a = [5, 6, 7, 10, 15, 19, 20, 22, 24, 27]
# max_num = a[0]
# for x in a:
#     if x > max_num:
#         max_num = x
# print(max_num)

#    0  1  2
# len = 3
# range(3) - 0 1 2
a = [1, 3, 2]

# for i in range(len(a)):
#     a[i] = 5

for x in a:
    print(x)

print(a)