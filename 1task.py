import json
import os

DATA_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(DATA_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter full Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    contacts = load_contacts()
    if contacts:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
    else:
        print("No contacts found.")

def search_contact():
    search_name = input("Enter the name to search: ")
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Found: {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def delete_contact():
    delete_name = input("Enter the name to delete: ")
    contacts = load_contacts()
    new_contacts = [contact for contact in contacts if contact['name'].lower() != delete_name.lower()]
    if len(contacts) == len(new_contacts):
        print("Contact not found.")
    else:
        save_contacts(new_contacts)
        print(f"Contact '{delete_name}' deleted successfully.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
