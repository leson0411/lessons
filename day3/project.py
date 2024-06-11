name = input("Enter the employee name: ")
name = name.strip()
name = name.title()

hourly_wage = float(input("Enter the hourly wage: "))
hours_worked = float(input("Enter the hours worked: "))

earning = hourly_wage * hours_worked

print(f"{name} earned ${earning:.2f} this week.")
