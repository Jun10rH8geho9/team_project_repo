from datetime import datetime


class Contact:
    def __init__(self, name, address, phone_number, email, birth_date):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()


class PersonalAssistant:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print('There are no contacts added.')
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Address: {contact.address} Phone: {contact.phone_number}, Email: {contact.email}, Birth date: {contact.birth_date.strftime('%d.%m.%Y')})")

    def upcoming_birthdays(self, days):
        today = datetime.today().date()
        upcoming_birthdays = [contact for contact in self.contacts if (contact.birth_date - today).days == days]
        if not upcoming_birthdays:
            print(f'There are no upcoming birthdays in {days} days.')
        else:
            print(f'Upcoming birthdays in {days} days: ')
            for contact in upcoming_birthdays:
                print(f"Name: {contact.name}, Birth date: {contact.birth_date.strftime('%d.%m.%Y')}")


assistant = PersonalAssistant()

while True:
    user_input = input('Enter the command (add / display / birthdays / exit): ')
    if user_input == 'exit':
        break

    elif user_input == 'add':
        name = input('Enter the name: ')
        address = input('Enter the address: ')
        phone_number = input('Enter the phone number: ')
        email = input('Enter the email: ')
        birth_date = input('Enter the date of birth in the following format <dd.mm.yyyy>: ')

        new_contact = Contact(name, address, phone_number, email, birth_date)
        assistant.add_contact(new_contact)

    elif user_input == 'display':
        assistant.display_contacts()

    elif user_input == 'birthdays':
        days = int(input('Enter the number of days for upcoming birthdays: '))
        assistant.upcoming_birthdays(days)


