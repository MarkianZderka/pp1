amount = float(input("Please enter the amount of money paid: "))
vat = amount * 0.23

formattedAmount = "{:.2f}".format(amount)
formattedVat = "{:.2f}".format(vat)

print(f"Amount: {formattedAmount}")
print(f"VAT: {formattedVat}")