first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username = f"{first[0]}{last}".lower()

fullname = f"{first} {last}".title()

#count displays the number of characters in the fullname
count = len(fullname)

# replace an ocurrence of i am with i'm using .replace()
fullname = fullname.replace("I am", "I'm")

print(f"your generated username is : {username.lower()}")

print("##################-------------------#############")

print(f"your fullname is : {fullname}")

print("####################--------------------############")

print(f"the number of characters in your fullname is : {count}")
