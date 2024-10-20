from contacts import add_contact, change_contact, show_phone, show_all  

    
def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").lower()
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                args = input("Enter name and phone: ").split()
                print(add_contact(args))
            case "change":
                args = input("Enter name and new phone: ").split()
                print(change_contact(args))
            case "phone":
                args = input("Enter name: ").split()
                print(show_phone(args))
            case "all":
                print(show_all())
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()