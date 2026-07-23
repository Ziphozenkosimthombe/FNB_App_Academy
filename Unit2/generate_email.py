# creating the profesional system email generated from the first and last name of the user  


first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()



username = f"{first[0]}{last}".lower()

print(f"your generated email is : {username.lower()}@fnb.co.za")
