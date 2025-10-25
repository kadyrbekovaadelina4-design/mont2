class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10

    def __str__(self):
        return f"{self.name}: {self.phone_number}"


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
            print(f"Контакт {name} успешно добавлен.")
        else:
            raise ValueError("Некорректный номер телефона. Должно быть ровно 10 цифр.")

    @classmethod
    def show_all_contacts(cls):
        if not cls.all_contacts:
            print("Список контактов пуст.")
        else:
            for contact in cls.all_contacts:
                print(contact)


ContactList.add_contact("Алиса", "9123456789")

ContactList.add_contact("Алиса", "9123456789")

ContactList.add_contact("Алиса", "9123456789")

ContactList.add_contact("Алиса", "9123456789")

# ContactList.add_contact("Боб", "12345")  # ошибку

ContactList.show_all_contacts()
