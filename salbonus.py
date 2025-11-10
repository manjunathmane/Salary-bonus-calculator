import sys
if len(sys.argv) ==3:
  script_name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("User provided input values:")

else:
  script_name = sys.argv[0]
  name = "Manjunath"
  rollno = "101"
  print("No input given - using default values:")

print("Script Name:", script_name)
print("Student Name:", name)
print("Roll Number:", rollno)


salary = sys.argv[0]
bonus = sys.argv[1]
total_salary = salary + bonus



salary = float(input("Enter the employee's salary: "))
bonus = 0.10 * salary
total_salary = salary + bonus
print("Bonus Amount: ₹", bonus)
print("Total Salary: ₹", total_salary)
