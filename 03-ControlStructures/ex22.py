name = input("Enter name: ")

lastLetter = name[-1]
if lastLetter == "a":
    print(f"{name} - Polish female name")
else:
    print(f"{name} – Polish male name")