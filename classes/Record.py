from classes import Name, Phone, Birthday
from .customErrors import PhoneValidationError
from helpers.wrappers import input_error

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def __str__(self):
        name = f"name: {self.name.value}"
        phones = f"phones: {'; '.join(p.value for p in self.phones if p.value)}"
        birthday = f"birthday: {self.birthday if self.birthday else ''}"
        return f"Contact {name}, {phones}, {birthday}"

    @input_error
    def add_phone(self, phone_number: str):
        if not [phone for phone in self.phones if phone.value == phone_number]:
            self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number:str) -> Phone:
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone:str, new_phone:str):
        found_phone = self.find_phone(old_phone)
        if not found_phone:
            raise PhoneValidationError("Phone number not found")
        found_phone.edit_phone(new_phone)

    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)

