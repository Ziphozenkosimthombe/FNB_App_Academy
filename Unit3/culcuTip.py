# clculating tip

bill = float(input("Enter the total bill amount: R"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount

#printing the tip amount and total amount

print(f"Tip amount: R{tip_amount}")
print(f"Tip amount: R{round(tip_amount, 2)} round off to 2 decimal places")

print(f"Total amount to be paid: R{total_amount}")
print(f"Total amount to be paid: R{round(total_amount, 2)} round off to 2 decimal places")