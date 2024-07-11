employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total = 0

for _, _, wage in employees:
    total = total + wage

avg = total / len(employees)

for emp in employees:
    if emp[2] > avg:
        print(emp[0])
