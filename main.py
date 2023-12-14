from datetime import datetime, timedelta
from rich.console import Console

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

    def add_contact(self, name, address, phone, email, birthday):
        # Додавання нового контакту
        pass

    def list_contacts(self):
        # Виведення списку контактів
        pass

    def search_contacts(self, query):
        # Пошук контактів за запитом
        pass

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
        # Аналіз введеного тексту користувача та визначення найближчої команди
        pass

# Приклад використання
assistant = PersonalAssistant()

while True:
    user_input = input("Введіть команду: ")
    assistant.analyze_user_input(user_input)
