basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
deduction = float(input("Enter deductions: "))

gross = basic + allowance + overtime
net = gross - deduction

print("Gross Salary =", gross)
print("Net Salary =", net)