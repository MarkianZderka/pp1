phonenumber = input("Enter phone number: ")

formattedPhoneNumber = f"{phonenumber[0:3]}-{phonenumber[3:6]}-{phonenumber[6:]}"

print(f"Phone number {formattedPhoneNumber}")