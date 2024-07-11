employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total = 0
num = 0

for i in range(len(employees)):
    emp = employees[i]
    total = total + emp[2]
    num += 1

avg = total / num

for i in range(len(employees)):
    emp_1 = employees[i]
    if emp_1[2] > avg:
        print(emp_1[0])
