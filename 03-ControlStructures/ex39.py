a = int(input("Enter side a: "))
b = int(input("Enter side b: "))


for i in range(a):
    if i == 0 or i == a - 1:
        print("*" * b)  
    else:
        print("*" + " " * (b - 2) + "*")  