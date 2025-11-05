income = int (input("Enter your monthly income: "))
total_expense = int (input("Enter your total monthly expenses: "))
monthly_saving = income - total_expense
print("Your monthly savings are $",monthly_saving)
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",projected_savings) 