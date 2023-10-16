from constants import COMMANDS

class InvalidCommandException(Exception):
    pass

def main():
    print("Welcome to the assitant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        try:
            if command == "hello":
                print("How can I help you?")
            elif "add" in command:
                #TODO add function add_contact
                print("Contact added")
            elif "change" in command:
                # TODO add func update_contact
                print("Contact updated.")
            elif "phone" in command:
                # TODO func getting and showing phone number of the person or error
                pass
            elif command.startswith("all"):
                # TODO function retrieving and presenting all saved contacts
                pass
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