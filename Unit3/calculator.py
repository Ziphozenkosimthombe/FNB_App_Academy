#calculator that two numbers as input
# and perform four arithmetic operations plus two advanced operations.
#must handle user input safely using type casting and display results clearly using f-strings.



num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

#Performing arithmetic operations
addition = num_1 + num_2
subtraction = num_1 - num_2
multiplication = num_1 * num_2
division = num_1 / num_2

#Performing advanced operations
floor_division = num_1 // num_2
modulus = num_1 % num_2

print(f"Addition: {num_1} + {num_2} = {round(addition, 2)} round off to 2 decimal places")
print(f"Subtraction: {num_1} - {num_2} = {round(subtraction, 2)} round off to 2 decimal places")
print(f"Multiplication: {num_1} * {num_2} = {round(multiplication, 2)} round off to 2 decimal places")
if num_2 == 0:
    print("Division: Division by zero is not allowed.")
else:
    print(f"Division: {num_1} / {num_2} = {round(division, 2)} round off to 2 decimal places")
    print(f"Floor Division: {num_1} // {num_2} = {round(floor_division, 2)} round off to 2 decimal places")
print(f"Modulus: {num_1} % {num_2} = {round(modulus, 2)} round off to 2 decimal places")