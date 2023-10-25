a1 = 0
a2 = 1
i = 0

while i < 20:
    i = i + 1
    a1, a2 = a2, a1 + a2
    print(f"{a1, a2}" ,end='')