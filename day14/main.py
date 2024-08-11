"""
1. open
2. process
3. close
"""
from pprint import pprint

# fo = open("data.txt", mode='r')

# ans = fo.read()
# print(ans)

# new = []
#
# for line in fo:
#     new.append(line.strip())
#
# print(new)

# print(fo.readline())

# fo.close()

# with open("data.txt", mode='w') as fo:
#     fo.write(str(123))

lst = []

with open("iris.csv") as csv_file:
    header = csv_file.readline().strip().split(',')

    for line in csv_file:
        values = line.strip().split(',')
        lst.append(dict(zip(header, values)))

pprint(lst)
