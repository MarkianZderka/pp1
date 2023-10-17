enterName = input("Enter name: ")

formattedName = []

for char in enterName:
    formattedName.append(ord(char))

print(f"Name: {enterName}")
print(" ".join([f"{char}({ord(char)})" for char in enterName]))
