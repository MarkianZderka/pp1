cardNumber = input("Enter card number: ")

formattedCardNumber = f"{cardNumber[0:4]}-{cardNumber[4:8]}-{cardNumber[8:12]}-{cardNumber[12:]}"

print(f"Card number {formattedCardNumber}")
