
import json


def add_contact(contacts):

    name = input("Enter a new name:")
    phone = input("Enter a phone:")
    email = input("Enter a email:")


    contact = {"name": name, "phone": phone, "email": email}

    contacts.append(contact)

def list_contacts(contacts):
    if not contacts:
        print("The list is empty")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(" ")

def search_contact(contacts):
    search = input("Enter the contact that you want to search:")
    found = False
    for contact in contacts:
        if contact["name"].strip().lower() == search.strip().lower():
            print(f"Found: {contact['name']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
    if not found:
            print("This contact is not on the list")

def delete_contact(contacts):
    delete = input("Which contact you want to delete?:")
    for contact in contacts:
        if contact["name"].strip().lower() == delete.strip().lower():
            contacts.remove(contact)
            print(f"{contact['name']} successfully deleted")
            return
    print("This contact is not on the list")

file_path = "contacts.json"

def save_contacts(contacts):
        with open(file_path, "w") as file:
            json.dump(contacts, file, indent=4)

def load_contacts():
    
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]

contacts = []

contacts = load_contacts()

while True:
    print("1.Add")
    print("2.Search")
    print("3.List")
    print("4.Delete")
    print("5.Exit")
    choice = input("Choose an option:")

    if choice == "1":
        add_contact(contacts)
        save_contacts(contacts)
    elif choice == "2":
        search_contact(contacts)
    elif choice == "3":
        list_contacts(contacts)
    elif choice == "4":
        delete_contact(contacts)
        save_contacts(contacts)
    elif choice == "5":
        break
    else:
        print("It doesn't exist")