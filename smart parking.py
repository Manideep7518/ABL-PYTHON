entry = int(input("Enter entry hour (24-hour format): "))
exit_time = int(input("Enter exit hour (24-hour format): "))

hours = exit_time - entry
fee = hours * 20

print("Parking Fee = ₹", fee)