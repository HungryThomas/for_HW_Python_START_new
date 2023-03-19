import os.path
 
def import_data(filename):
    phonebook = {}
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            for line in f:
                name, surname, number = line.strip().split(',')
                phonebook[name + ' ' + surname] = number
        print('Data imported successfully!')
    else:
        print('File not found.')
    return phonebook
 
def export_data(filename, phonebook):
    with open(filename, 'w') as f:
        for name, number in phonebook.items():
            surname = name.split()[1]
            f.write(','.join([name.split()[0], surname, number]) + '\n')
    print('Data exported successfully!')
 
def create_contact(phonebook):
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    number = input('Enter phone number: ')
    phonebook[name + ' ' + surname] = number
    print('Contact created successfully!')
 
def update_contact(phonebook):
    name = input('Enter name of contact to update: ')
    surname = input('Enter surname of contact to update: ')
    if name + ' ' + surname in phonebook:
        new_number = input('Enter new phone number: ')
        phonebook[name + ' ' + surname] = new_number
        print('Contact updated successfully!')
    else:
        print('Contact not found.')
 
def delete_contact(phonebook):
    name = input('Enter name of contact to delete: ')
    surname = input('Enter surname of contact to delete: ')
    if name + ' ' + surname in phonebook:
        del phonebook[name + ' ' + surname]
        print('Contact deleted successfully!')
    else:
        print('Contact not found.')
 
def display_menu():
    print('1. Create contact')
    print('2. Update contact')
    print('3. Delete contact')
    print('4. Display all contacts')
    print('5. Import data')
    print('6. Export data')
    print('0. Exit')
 
def display_contacts(phonebook):
    for name, number in phonebook.items():
        print(name + ': ' + number)
 
def main():
    phonebook = {}
    while True:
        display_menu()
        choice = input('Enter choice: ')
        if choice == '1':
            create_contact(phonebook)
        elif choice == '2':
            update_contact(phonebook)
        elif choice == '3':
            delete_contact(phonebook)
        elif choice == '4':
            display_contacts(phonebook)
        elif choice == '5':
            filename = input('Enter filename: ')
            phonebook = import_data(filename)
        elif choice == '6':
            filename = input('Enter filename: ')
            export_data(filename, phonebook)
        elif choice == '0':
            break
        else:
            print('Invalid choice.')
 
if __name__ == '__main__':
    main()