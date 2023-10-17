import math

a = float(input("Enter the length of the side A: "))
b = float(input("Enter the length of the side B: "))
c = float(input("Enter the lenght of the side C: "))

p = (a + b + c) / 2 
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
circumference = a + b + c

print(f"The are of the triangle is: {S}, and the circumference is {circumference}")
