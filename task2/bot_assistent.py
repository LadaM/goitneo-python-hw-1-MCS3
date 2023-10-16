import json
from constants import COMMANDS, CONTACTS_FILE
from pathlib import Path

def main():
    print("Welcome to the assitant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        try:
            if command == "hello":
                print("How can I help you?")
            elif command.startswith("add"):
                try:
                    _, name, phone = command.split()
                    add_contact(name, phone)
                    print("Contact added")
                except ValueError:
                    print(f"Expecting command in form {COMMANDS.get('add')}")
                    continue
            elif command.startswith("change"):
                update_contact(command)
                print("Contact updated.")
            elif command.startswith("phone"):
                show_contact(command)
            elif command.startswith("all"):
                show_all_contacts()
            elif command in ["close", "exit"]:
                print("Good bye!")
                break
            else:
                raise InvalidCommandException
        except InvalidCommandException:
            print(("Ivalid command recieved. Accepted commands are:\n{}"
                   .format('\n'.join(['- ' + s for s in COMMANDS.values()]))))
            continue


class InvalidCommandException(Exception):
    pass


def add_contact(name: str, phone: str):
    file_path = Path.cwd().joinpath(CONTACTS_FILE)
    contact = {
        "name": name,
        "phone": phone
    }
    with open(file_path, 'w+') as file:
        json.dump(contact, file)

def update_contact(command):
    pass


def show_all_contacts(command):
    pass


def show_contact(command):
    pass


if __name__ == "__main__":
    main()
