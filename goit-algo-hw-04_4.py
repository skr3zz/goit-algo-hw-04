def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use 'add [name] [phone]'"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use 'change [name] [new_phone]'"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated successfully"

def show_contact(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use 'show [name]'"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command format. Use 'phone [name]'")
            else:
                name = args[0]
                if name not in contacts:
                    print("Contact not found.")
                else:
                    print(f"Phone number for {name}: {contacts[name]}")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
