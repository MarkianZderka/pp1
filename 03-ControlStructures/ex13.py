number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > 0 and number2 > 0:
    print(f"Both {number1} and {number2} are positive")
else:
    print(f"At least one of entered numbers {number1} and {number2} is not negative")