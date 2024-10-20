contacts = {}

def add_contact(args):  
    # Додає контакт до словника.
    if len(args) == 2:  
        name, phone = args  
        contacts[name] = phone  
        return f"Contact {name} added."  
    else:  
        return "Error: Please provide both a name and a phone number."  

def change_contact(args):  
    # Змінює номер телефону контакту. 
    if len(args) == 2:  
        name, new_phone = args  
        if name in contacts:  
            contacts[name] = new_phone  
            return f"Contact {name} updated."  
        else:  
            return f"Error: Contact {name} not found."  
    else:  
        return "Error: Please provide both a name and a new phone number."  

def show_phone(args):  
    # Показує номер телефону для вказаного контакту.
    if len(args) == 1:  
        name = args[0]  
        if name in contacts:  
            return f"{name}'s phone number is {contacts[name]}."  
        else:  
            return f"Error: Contact {name} not found."  
    else:  
        return "Error: Please provide a contact name."  

def show_all():  
    # Показує всі контакти. 
    if contacts:  
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])  
    else:  
        return "No contacts found."  