
binaryNumber = input("Enter a 4-digit binary number: ")


if len(binaryNumber) == 4 and binaryNumber.isdigit() and all(bit in "01" for bit in binaryNumber):
    decimal_value = 0

    
    for i in range(4):
        decimal_value += int(binaryNumber[3 - i]) * (2 ** i)

    print(f"Binary: {binaryNumber}")
    print(f"Decimal: {decimal_value}")

