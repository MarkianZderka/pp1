heightCm = 195

heightFeet = heightCm // 30.48
heightInches = (heightCm / 30.48 - heightFeet) * 12

print(f"I am {heightCm}cm tall. Or {heightFeet}ft {round(heightInches)} in")