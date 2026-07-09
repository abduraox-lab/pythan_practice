contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(name, "-", phone)

    elif choice == "3":
        search_name = input("Enter contact name to search: ")
        if search_name in contacts:
            print(search_name, "-", contacts[search_name])
        else:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter contact name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")