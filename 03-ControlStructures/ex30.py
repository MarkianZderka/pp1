hour24 = input("Enter time (24-hour format): ")

Hour = int(hour24[0:2])
Minutes = (hour24[3:])

hour12 = (f"{Hour-12}:{Minutes}")

if Hour in range(12, 25):
    print(f"Time in 12h format: {hour12} pm")
else:
    print(f"Time in 12h format: {hour12} am")