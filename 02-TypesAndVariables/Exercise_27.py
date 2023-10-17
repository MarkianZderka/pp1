number = int(input("Enter the number"))

isInRange = True
if number <= -10 or number >= 10:  
    isInRange = False

print(f"The number {number} is in range [-10; 10] {isInRange}")