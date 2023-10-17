vehicleNumber = input("PLease enter the vehicle registration number: ")

isFromKrakow =  vehicleNumber.startswith("KR") or vehicleNumber.startswith("KK")

print(f"Car from Krakow: {isFromKrakow}")
