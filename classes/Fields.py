import re
from datetime import datetime
from .customErrors import ShortName, PhoneValidationError, DateFormatError
# from birthday_helpers import get_datetime_from_str
from helpers.constants import format

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):
        Name.check_name(name)
        super().__init__(name)
        self.value = name.strip()

    def edit_name(self, new_name: str):
        Name.check_name(new_name)
        self.value = new_name.strip()

    @staticmethod
    def check_name(name: str):
        if (len(name.strip())<2):
            raise ShortName("Name should be at least 2 chars")

class Phone(Field):
    def __init__(self, phone: str):
        Phone.validate_phone(phone)
        super().__init__(phone)
        self.value = phone

    def edit_phone(self, new_phone: str):
        Phone.validate_phone(new_phone)
        self.value = new_phone

    @staticmethod
    def validate_phone(phone: str):
        pattern = r"^\d{10}$"
        check = re.search(pattern, phone.strip())
        if not check:
            raise PhoneValidationError("Phone should be 10 digits")

class Birthday(Field):
    def __init__(self, value: str):
        try:
            birthday = datetime.strptime(value.strip(), format).date()
            today = datetime.today().date()
            if birthday > today:
                raise DateFormatError("Invalid date, after today")
            self.value = birthday
        except ValueError as err:
            if str(err).find("format") != -1:
                raise DateFormatError("Invalid date format. Use DD.MM.YYYY")
            raise ValueError(err)

    def __str__(self):
        return datetime.strftime(self.value, format)
