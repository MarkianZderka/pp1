name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

age1 = int(input(f"Enter {name1} age: "))
age2 = int(input(f"Enter {name2} age: "))

if age1 >= 18 and age2 >= 18:
    print(f"Both {name1} and {name2} are adults")

if age1 < 18 and age2 < 18:
     print(f"Both {name1} and {name2} are minors")

if age1 >= 18 and age2 < 18:
      print(f"{name1} is adult {name2} is minor")

if age1 < 18 and age2 >= 18:
      print(f"{name1} is minor {name2} is adult")