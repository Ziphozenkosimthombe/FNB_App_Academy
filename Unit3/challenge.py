# The South African Fuel Cost Calculator

# 1. Ask the user how many kilometers they want to drive
kilometers = float(input("How many kilometers do you want to drive? "))

# 2. Ask for the current petrol price per liter
petrol_price = float(input("What is the current petrol price per liter (e.g. 22.45)? "))

# 3. Calculate liters needed (1 liter per 10 km)
liters_needed = kilometers / 10

# 4. Calculate the total cost
total_cost = liters_needed * petrol_price

# 5. Round the final cost to 2 decimal places
total_cost = round(total_cost, 2)

# Display the result
print(f"\nTo drive {kilometers} km, you'll need {round(liters_needed, 2)} liters of fuel.")
print(f"Total estimated cost: R{total_cost}")