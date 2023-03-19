import os
 
phonebook = {}
 
def create_contact():
    name = input("Enter contact name: ")
    surname = input("Enter contact surname: ")
    phone_number = input("Enter contact phone number: ")
    phonebook[name] = {"surname": surname, "phone_number": phone_number}
    print('Contact has been added to the phonebook.')
 
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in phonebook:
        surname = input("Enter contact surname: ")
        phone_number = input("Enter contact phone number: ")
        phonebook[name]["surname"] = surname
        phonebook[name]["phone_number"] = phone_number
        print('Contact details have been updated.')
    else:
        print('Contact is not in the phonebook.')
 
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in phonebook:
        del phonebook[name]
        print('Contact has been deleted from the phonebook.')
    else:
        print('Contact is not in the phonebook.')
 
def display_contacts():
    if phonebook:
        for name in phonebook:
            print(name)
    else:
        print("The phonebook is empty.")
 
def import_contacts():
    filename = input("Enter the name of the file to import: ")
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            for line in file:
                name, surname, phone_number = line.strip().split(",")
                phonebook[name] = {"surname": surname, "phone_number": phone_number}
        print('Contacts have been imported.')
    else:
        print('The file does not exist.')
 
def export_contacts():
    filename = input("Enter the name of the file to export: ")
    with open(filename, "w") as file:
        for name in phonebook:
            file.write(name)
    print('contacts have been exported.')
 
def main():
    while True:
        print("Menu:\n1. Create contact\n2. Update contact\n3. Delete contact\n4. Display contacts\n5. Import contacts\n6. Export contacts\n7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            import_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
 
if __name__ == "__main__":
    main()