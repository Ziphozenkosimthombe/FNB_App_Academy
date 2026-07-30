# 1. Dictionary of contacts: name -> phone number (as string)
contacts = {
    "Sarah": "0821112222",
    "Mandla": "0837654321",
    "Priya": "0719998888",
}

# 2. Ask the user for a name to look up
name = input("Enter the name of the friend you want to look up: ").strip()

# 3. Check if the name exists as a key, and print accordingly
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")