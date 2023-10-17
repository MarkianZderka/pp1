password = input("Please enter password: ")

requiredAmount = 8
amountInPassword = len(password)

passwordIsCorrect = False
if amountInPassword >= requiredAmount:
    passwordIsCorrect = True

print(f"The password is valid: {passwordIsCorrect}")
