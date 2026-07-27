"""
Command-Line Contact Book
---------------------------
Stores contacts as a list of dictionaries (name, phone, email) and lets
the user add, search, view, and delete contacts through a menu.
"""

# The list of dictionaries that stores all contacts
contacts = []


def add_contact():
    """Ask the user for details and append a new contact dictionary to the list."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    print(f"\nContact '{name}' added successfully!")


def search_contact(name):
    """Search the contacts list by name. Return the matching dictionary, or None."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    """Remove a contact from the list by name. Print whether it succeeded."""
    contact = search_contact(name)
    if contact is not None:
        contacts.remove(contact)
        print(f"\nContact '{name}' deleted successfully!")
    else:
        print(f"\nNo contact found with the name '{name}'.")


def view_all():
    """Display all contacts in a formatted layout."""
    if not contacts:
        print("\nNo contacts saved yet.")
        return

    print("\n" + "=" * 45)
    print(f"{'CONTACT BOOK':^45}")
    print("=" * 45)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name : {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 45)


def print_menu():
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            name = input("Enter the name to search for: ")
            result = search_contact(name)
            if result is not None:
                print("\nContact found:")
                print(f"Name : {result['name']}")
                print(f"Phone: {result['phone']}")
                print(f"Email: {result['email']}")
            else:
                print(f"\nNo contact found with the name '{name}'.")

        elif choice == "3":
            name = input("Enter the name to delete: ")
            delete_contact(name)

        elif choice == "4":
            view_all()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()