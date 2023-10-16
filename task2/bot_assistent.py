from constants import COMMANDS

class InvalidCommandException(Exception):
    pass

def add_contact(command):
    pass

def update_contact(command):
    pass

def show_all_contacts(command):
    pass

def show_contact(command):
    pass

def main():
    print("Welcome to the assitant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        try:
            if command == "hello":
                print("How can I help you?")
            elif command.startswith("add"):
                add_contact(command)
                print("Contact added")
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
                   .format('\n'.join(['- ' + s for s in COMMANDS]))))
            continue

if __name__ == "__main__":
    main()