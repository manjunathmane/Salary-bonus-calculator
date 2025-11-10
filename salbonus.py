import sys
if len(sys.argv) ==2:
  salary = sys.argv[0]
  bonus = sys.argv[1]
  total_salary = salary + bonus
  print("User provided input values:")

else:
  salary = 50000
  bonus = 0.10 * salary
  total_salary = salary + bonus
  print("Bonus Amount: ₹", bonus)
  print("Total Salary: ₹", total_salary)



