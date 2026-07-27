"""
The Smart ATM Withdrawal Simulator
------------------------------------
Simulates a bank transaction, checking if a user has enough money
to make a withdrawal.
"""

# 1. Set a fixed variable representing a bank balance
balance = 500

# 2. Ask the user how much money they want to withdraw
withdrawal_amount = float(input("How much money would you like to withdraw? R"))

# 4. If the request is less than or equal to 0, print an invalid amount message
if withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than \"R0\".")

# 3. If the request is less than or equal to the balance, deduct and print success
elif withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")

# 5. Otherwise, the balance is insufficient
else:
    print("Declined. Insufficient funds")