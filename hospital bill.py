consultation = float(input("Enter consultation fee: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

total = consultation + diagnostic + treatment

print("Total Bill =", total)

if total > 5000:
    print("Patient Category = Premium")
else:
    print("Patient Category = Regular")