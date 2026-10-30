balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")
