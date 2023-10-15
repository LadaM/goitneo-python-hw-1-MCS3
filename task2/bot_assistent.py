def handle_command(command: str):
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
    elif command.startswith("close") or command.startswith("exit"):
        print("Good bye!")
    else: 
        # TODO raise error? or just give back something 
        print("Invalid command.")

def main():
    print("Welcome to the assitant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        try:
            handle_command(command=command)
        except:
            print("Oops... Some error happenned")
            continue

if __name__ == "__main__":
    main()