from contact import Contact,ContactList

def add_contact(contact_list):
    name = input("Enter contact name: ").strip()
    number = input("Enter contact number: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    if not number:
        raise ValueError("Number cannot be empty.")

    contact = Contact(name, number)
    contact_list.add_contact(contact)

    print("Contact added successfully.")


def list_contacts(contact_list):
    contact_list.list_contacts()


def update_contact(contact_list):
    current_name = input(
        "Enter the name of the contact to update: "
    ).strip()

    new_name = input("Enter new name: ").strip()
    new_number = input("Enter new number: ").strip()

    if not new_name:
        raise ValueError("Name cannot be empty.")

    if not new_number:
        raise ValueError("Number cannot be empty.")

    contact_list.update_contact(
        current_name,
        new_name,
        new_number
    )

    print("Contact updated successfully.")


def remove_contact(contact_list):
    name = input(
        "Enter the name of the contact to remove: "
    ).strip()

    contact_list.remove_contact(name)

    print("Contact removed successfully.")

def main():
    contact_list = ContactList()

    while True:
        print("\n============= Contact List Menu =============")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Update Contact")
        print("4. Remove Contact")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > 5:
                raise ValueError("Choice must be between 1 and 5.")

            if choice == 1:
                add_contact(contact_list)

            elif choice == 2:
                list_contacts(contact_list)

            elif choice == 3:
                update_contact(contact_list)

            elif choice == 4:
                remove_contact(contact_list)

            elif choice == 5:
                print("Exiting...")
                break

        except ValueError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()