fathersSalary = float(input("Enter fathers salary: "))
mothersSalary = float(input("Enter mothers salary: "))
numberOfFamilyMembers = float(input("Enter number of people in family: "))

totalIncome = fathersSalary + mothersSalary

incomePerPerson = totalIncome / numberOfFamilyMembers

print(f"The income per person is:  {incomePerPerson}")