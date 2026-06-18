contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added successfully!")

    elif choice == "2":
        if contacts:
            print("\nContacts:")
            for name, number in contacts.items():
                print(name, ":", number)
        else:
            print("No contacts available.")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice!")
