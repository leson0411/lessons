employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for i in range(len(employees)):
    name, hours_worked, hourly_wage = employees[i]
    paid = hours_worked * hourly_wage
    print(f"{name} is paid {paid:.2f} per week")
