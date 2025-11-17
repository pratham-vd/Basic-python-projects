contacts = []  

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact added!")

    # Search contact
    elif choice == "2":
        search_name = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c["name"].lower() == search_name.lower():
                print("Found:", c["name"], "-", c["phone"])
                found = True
        if not found:
            print("Contact not found.")

    # Delete contact
    elif choice == "3":
        delete_name = input("Enter name to delete: ")
        deleted = False
        for c in contacts:
            if c["name"].lower() == delete_name.lower():
                contacts.remove(c)
                print("Contact deleted!")
                deleted = True
                break
        if not deleted:
            print("No such contact.")

    # Show all contacts
    elif choice == "4":
        print("\nAll Contacts:")
        for c in contacts:
            print(c["name"], "-", c["phone"])
        if len(contacts) == 0:
            print("No contacts yet.")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
