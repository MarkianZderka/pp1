height = int(input("Enter the heigt: "))
weight = int(input("Enter the weight"))

bmi = weight / (height / 100) ** 2

bmiIsGood = True
if bmi <= 18.5 or bmi >= 24.9:
   bmiIsGood = False

print(f"Your BMI value is {bmi} is healthy: {bmiIsGood}")

