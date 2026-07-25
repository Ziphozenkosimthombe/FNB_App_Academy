#create a script that helps users to show a secure password

password = input("Enter your password: ")
white_space = password.strip()
first_letter = password[0]
#grabbing the last letter of the password
last_letter = password[-1]

#replacing the first letter of the password with a * and the last letter with a *
# secure_password = password.replace(first_letter, first_letter.upper(), 1).replace(last_letter, last_letter.upper(), 1)
print(f"your password before : {password}")
print(f"your secure password start with : {first_letter.upper()} and ends with : {last_letter.upper()}")