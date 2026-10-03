class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}"


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        contact_display = [
            f"{index + 1}. {contact.name} - {contact.number}"
            for index, contact in enumerate(self.contacts)
        ]

        for contact in contact_display:
            print(contact)

    def update_contact(self, current_name, new_name, new_number):
        for contact in self.contacts:
            if contact.name == current_name:
                contact.name = new_name
                contact.number = new_number
                return

        raise ValueError("Contact not found.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return

        raise ValueError("Contact not found.")

