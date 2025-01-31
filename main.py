from classes import AddressBook, Record
from helpers import book_operations

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main(test_users = None):
    book = AddressBook()
    if test_users:
        for user in test_users:
            rec = Record(user['name'])
            rec.add_phone(user['phone'])
            rec.add_birthday(user['birthday'])
            book.add_record(rec)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "all":
                print(book_operations.get_all_contacts(book))
            case "add":
                print(book_operations.add_contact(args, book))
            case "change":
                print(book_operations.change_contact(args, book))
            case "phone":
                print(book_operations.get_contact_phones(args, book))
            case"add-birthday":
                print(book_operations.add_birthday(args, book))
            case "show-birthday":
                print(book_operations.show_birthday(args, book))
            case "birthdays":
                print(book_operations.get_birthdays(book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    users = [
        {"name": "Doe", "phone": "0123456789", "birthday": "21.01.1985"},
        {"name": "John", "phone": "0987654321", "birthday": "22.01.1985"},
        {"name": "John Doe", "phone": "7894561230", "birthday": "23.01.1985"},
        {"name": "Jane Smith", "phone": "1234567890", "birthday": "27.01.1990"},
        {"name": "Jane", "phone": "3216549870", "birthday": "28.01.1990"},
        {"name": "Smith", "phone": "0321654987", "birthday": "29.01.1990"}
    ]
    main(users)