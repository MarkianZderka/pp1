carSpeed = int(input("Enter how fast the car is going: "))

speedIsLegal = True
if carSpeed < 40 or carSpeed > 140:
    speedIsLegal = False

print(f"Speed is valid: {speedIsLegal}")
