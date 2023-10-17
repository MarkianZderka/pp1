import math

treeCircumference = int(input("Enter tree`s circumference in cm"))

treeDiameter = treeCircumference / math.pi

canBeCutDown = False
if treeDiameter >= 50:
    canBeCutDown = True

print(f"Tree can be cut down: {canBeCutDown}") 