from datetime import datetime, timedelta
from rich.console import Console
import re

console = Console()

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []

    def is_valid_phone(self, phone):
        # Перевірка правильності формату номера телефону
        # Допустимі формати: +380501234567, 050-123-45-67, 0501234567, (050)123-45-67
        phone_pattern = re.compile(r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$')
        return bool(re.match(phone_pattern, phone))

    def is_valid_email(self, email):
        # Перевірка правильності формату електронної пошти
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return bool(re.match(email_pattern, email))

    def add_contact(self, name, address, phone, email, birthday):
        # Додавання нового контакту
        if not self.is_valid_phone(phone):
            console.print("[bold red]Помилка:[/bold red] Некоректний номер телефону.")
            return

        if not self.is_valid_email(email):
            console.print("[bold red]Помилка:[/bold red] Некоректна електронна пошта.")
            return

        new_contact = Contact(name, address, phone, email, birthday)
        self.contacts.append(new_contact)
        console.print(f"[green]Контакт {name} успішно доданий до книги контактів.[/green]")

    def list_contacts(self):
        # Виведення списку контактів
        for idx, contact in enumerate(self.contacts):
            console.print(f"[cyan]Контакт #{idx + 1}[/cyan]")
            console.print(f"Ім'я: {contact.name}")
            console.print(f"Адреса: {contact.address}")
            console.print(f"Телефон: {contact.phone}")
            console.print(f"Електронна пошта: {contact.email}")
            console.print(f"Дата народження: {contact.birthday}")
            console.print("-" * 20)

    def search_contacts(self, query):
        # Пошук контактів за запитом
        result_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.address.lower() \
                    or query.lower() in contact.phone.lower() or query.lower() in contact.email.lower():
                result_contacts.append(contact)
        return result_contacts

    def edit_contact(self, contact_index, name, address, phone, email, birthday):
        # Редагування контакту
        pass

    def delete_contact(self, contact_index):
        # Видалення контакту
        pass

    def upcoming_birthdays(self, days):
        # Виведення списку контактів, дні народження яких наближаються
        pass

    def add_note(self, text, tags):
        # Додавання нової нотатки
        pass

    def list_notes(self):
        # Виведення списку нотаток
        pass

    def search_notes(self, query):
        # Пошук нотаток за запитом
        pass

    def edit_note(self, note_index, text, tags):
        # Редагування нотатки
        pass

    def delete_note(self, note_index):
        # Видалення нотатки
        pass

    def sort_notes_by_tags(self):
        # Сортування нотаток за тегами
        pass

    def categorize_files(self, folder_path):
        # Сортування файлів у зазначеній папці за категоріями
        pass

    def analyze_user_input(self, user_input):
        if "додати контакт" in user_input.lower():
            console.print("[green]Пропоную вам додати новий контакт. Використайте команду add_contact.[/green]")
        elif "список контактів" in user_input.lower():
            console.print("[green]Для виведення списку контактів використайте команду list_contacts.[/green]")
        

        else:
            console.print("[yellow]Не можу розпізнати вашу команду. Спробуйте ще раз.[/yellow]")


assistant = PersonalAssistant()

while True:
    user_input = input("Введіть команду: ")
    assistant.analyze_user_input(user_input)
