import json
import os
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
                    _, name, phone = command.split(' ')
                    add_contact(name, phone)
                    print("Contact added")
                except ValueError:
                    print(f"Expecting command in form {COMMANDS.get('add')}")
                except DuplicateEntry:
                    print(f"We alreay have a contact with name {name}")
            elif command.startswith("change"):
                try:
                    _, name, phone = command.split(' ')
                    update_contact(name, phone)
                    print("Contact updated")
                except ValueError:
                    print(f"Expecting command in form {COMMANDS.get('update')}")
                except ValueNotFound:
                    print(f"No contact for name {name} found")
            elif command.startswith("phone"):
                try:
                    _, name = command.split(' ')
                    phone = get_phone(name)
                    print(phone)
                except ValueError:
                    print(f"Expecting command in form {COMMANDS.get('phone')}")
                except ValueNotFound:
                    print(f"No contact for name {name} found")
            elif command.startswith("all"):
                try:
                    contacts = get_contacts()
                    for contact in contacts:
                        print(f"{contact.get('name'):<10}{contact.get('phone'):<10}")
                except FileNotFoundError:
                    # if the file is empty there are no contacts to show
                    print("We haven't stored any contacts yet")
            elif command in ["close", "exit"]:
                print("Goodbye!")
                break
            else:
                raise InvalidCommandException
        except InvalidCommandException:
            print(("Ivalid command recieved. Accepted commands are:\n{}"
                   .format('\n'.join(['- ' + s for s in COMMANDS.values()]))))
            continue

# exception when invalid commdand was entered by the user
class InvalidCommandException(Exception):
    pass

# exception raised when value wasn't found
class ValueNotFound(Exception):
    pass

class DuplicateEntry(Exception):
    pass

file_path = Path.cwd().joinpath(CONTACTS_FILE)

def add_contact(name: str, phone: str):
    try:
        contacts = get_contacts()
    except FileNotFoundError:
        # if there is no file yet or it is empty, we just create one and add contact
        contacts = []

    for c in contacts:
        # if we already have a name in our contact list, we don't add it again
        n = c.get("name")
        if n == name:
            raise DuplicateEntry
    
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    with open(file_path, 'w') as json_file:
        json.dump(contacts, json_file, indent=4)

def update_contact(name, phone):
    try:
        contacts = get_contacts()
        updated = False
        for c in contacts:
            if c.get("name") == name:
                c["phone"] = phone
                updated = True
        with open(file_path, 'w') as json_file:
            json.dump(contacts, json_file, indent=4)
        if not updated:
            raise ValueNotFound
    except FileNotFoundError:
        # if the file is empty, our name isn't in the file
        raise ValueNotFound

def get_phone(name):
    try:
        contacts = get_contacts()
        for c in contacts:
            if c.get("name") == name:
                return c["phone"]
        # if there was no match, then there is no such contact stored
        raise ValueNotFound
    except FileNotFoundError:
        # if the file is empty, our name isn't in the file
        raise ValueNotFound

def get_contacts():
    file_not_empty = os.path.isfile(file_path) and os.path.getsize(file_path) > 0
    if file_not_empty:
        with open(file_path, 'r') as json_file:
            data_list = json.load(json_file)
            return data_list
    else:
        raise FileNotFoundError

if __name__ == "__main__":
    main()