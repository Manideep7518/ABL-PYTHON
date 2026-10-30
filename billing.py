price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 3000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Final Bill = ₹", final_bill)