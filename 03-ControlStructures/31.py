x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print(f"Point P({x}, {y}) is in the first quadrant of the coordinate system.")

if x > 0 and y < 0:
    print(f"Point P({x}, {y}) is in the second quadrant of the coordinate system.")

if x < 0 and y > 0:
    print(f"Point P({x}, {y}) is in the fourth quadrant of the coordinate system.")

if x < 0 and y < 0:
    print(f"Point P({x}, {y}) is in the third quadrant of the coordinate system.")

if x == 0 and y == 0:
    print(f"Point P({x}, {y}) is in the centere of the coordinate system.")

if x == 0 or y == 0:
    print(f"Point P({x}, {y}) is on the one of the axises of the coordinate system.")