hour_worked = float(input("Enter the number of hour worked: "))
hourly_wage = float(input("Enter the employee's hourly wage: "))

total = hourly_wage * hour_worked

if hour_worked > 40:
    regular_pay = hourly_wage * 40
    overtime_pay = (hour_worked - 40) * hourly_wage * 1.1
    total = regular_pay + overtime_pay

print(f"The total pay of this employee is ${total:.2f}")

