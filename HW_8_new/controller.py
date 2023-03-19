phonebook = {}
 
# function to add a new contact to the phonebook
def add_contact():
    name = input("Enter the name of the new contact: ")
    number = input("Enter the phone number of the new contact: ")
    phonebook[name] = number
    print('contact added!')
 
# function to update an existing contact's phone number
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in phonebook:
        number = input("Enter the new phone number for this contact: ")
        phonebook[name] = number
        print('contact updated!')
    else:
        print('contact not found')
 
# function to remove a contact from the phonebook
def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in phonebook:
        del phonebook[name]
        print('deleted!')
    else:
        print('not found')
 
# function to display all contacts in the phonebook
def display_contacts():
    if not phonebook:
        print("The phonebook is empty.")
    else:
        print("Phonebook entries:")
        for name in phonebook.items():
            print(name)
 
# function to display the menu and get user input
def menu():
    print("\n\n*** Phonebook Menu ***")
    print("1. Add a new contact")
    print("2. Update an existing contact's phone number")
    print("3. Remove a contact from the phonebook")
    print("4. Display all contacts")
    print("5. Quit the program")
 
    choice = input("\nEnter your choice (1-5): ")
    return choice
 
# main program loop
while True:
    choice = menu()
 
    if choice == "1":
        add_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        remove_contact()
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1-5.")