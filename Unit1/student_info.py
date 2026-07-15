# student Info Formatter
#collects personal information from the user and displays it as a formatted profile card


#-------Collect input-----------
firstName = input("Enter your first name: ")
surname = input("Enter your last name: ")
age = int(input("Enter your age: "))
favoriteNumber = float(input("Enter your favorite number as a float: "))


# ---- string manipulation ----

full_name = f"{firstName} {surname}"
full_name_upper = full_name.upper()
full_name_title = full_name.title()


#---Arithmetic----
age_in_months = age * 12
rounded_favorite_number = round(favoriteNumber, 2   )

#-----output----

print()
print(f"Welcome, {full_name}")
print()
print("-------Profile Card-------")
print(f"Full Name (UPPERCASE): {full_name_upper}")
print(f"Full Name (Title Case): {full_name_title}")
print(f"Age: {age} years old")
print(f"Age in months: {age_in_months} months")
print(f"Favorite Number (rounded to 2 d.p.): {rounded_favorite_number}  ")


#--- Data types-----

print()
print("-------Data Types-------")
print(f"Type of first name: {type(firstName)}")
print(f"Type of surname: {type(surname)}")
print(f"Type of age: {type(age)}")
print(f"Type of favorite number: {type(favoriteNumber)}")