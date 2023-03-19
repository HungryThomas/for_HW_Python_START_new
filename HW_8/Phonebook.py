import csv
 
class Phonebook:
    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        self.load_data()
 
    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.entries.append({'name': row[0], 'surname': row[1], 'phone': row[2]})
        except FileNotFoundError:
            pass
 
    def save_data(self):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for entry in self.entries:
                writer.writerow([entry['name'], entry['surname'], entry['phone']])
 
    def add_entry(self):
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        phone = input("Enter phone number: ")
        self.entries.append({'name': name, 'surname': surname, 'phone': phone})
        self.save_data()
        print("Entry added successfully.")
 
    def update_entry(self):
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        for entry in self.entries:
            if entry['name'] == name and entry['surname'] == surname:
                phone = input("Enter new phone number: ")
                entry['phone'] = phone
                self.save_data()
                print("Entry updated successfully.")
                return
        print("Entry not found.")
 
    def delete_entry(self):
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        for i, entry in enumerate(self.entries):
            if entry['name'] == name and entry['surname'] == surname:
                del self.entries[i]
                self.save_data()
                print("Entry deleted successfully.")
                return
        print("Entry not found.")
 
    def display_menu(self):
        print("1. Add new entry")
        print("2. Update existing entry")
        print("3. Delete existing entry")
        print("4. Exit")
 
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_entry()
            elif choice == '2':
                self.update_entry()
            elif choice == '3':
                self.delete_entry()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")