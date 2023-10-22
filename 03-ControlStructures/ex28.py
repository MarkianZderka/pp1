EAN13 = str(input("Enter EAN-13 article number: ")).strip()

if len(EAN13) != 13:
    print("Enter valid number!")
    
else:
    print("Number is correct")

if "590" in EAN13:
    print("The product is from Poland.")