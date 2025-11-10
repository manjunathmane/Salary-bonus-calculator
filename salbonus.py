import sys
if len(sys.argv) ==3:
  salary = sys.argv[0]
  bonus = sys.argv[1]
  total_salary = salary + bonus
  print("User provided input values:")

else:
  salary = float(input("Enter the employee's salary: "))
  bonus = 0.10 * salary
  total_salary = salary + bonus
  print("Bonus Amount: ₹", bonus)
  print("Total Salary: ₹", total_salary)



