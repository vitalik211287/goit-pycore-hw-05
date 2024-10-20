from parser import parse_input  
from contacts import add_contact, change_contact, show_phone, show_all  

def main():  
    print("Welcome to the assistant bot!")  # Додаємо вітання  
    
    while True:  
        command_input = input("Enter a command: ")  # Отримуємо команду від користувача  
        cmd, args = parse_input(command_input)  # Парсимо команду та аргументи  
        
        if cmd in ["close", "exit"]:  
            print("Good bye!")  
            break  
        elif cmd == "hello":  
            print("How can I help you?")  
        elif cmd == "add":  
            print(add_contact(args))  
        elif cmd == "change":  
            print(change_contact(args))  
        elif cmd == "phone":  
            print(show_phone(args))  
        elif cmd == "all":  
            print(show_all())  
        else:  
            print("Invalid command.")  

if __name__ == "__main__":  
    main()