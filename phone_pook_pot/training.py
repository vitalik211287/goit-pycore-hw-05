def xxx ():
    print('Welcome')
    while True:
        command = input('enter command: ')
        match command:
                case "hello":
                    print('How can I help you?:')         
                case "open":
                    args = input('enter name: ')
                    print(f"'its open, {args}'")
                case "close":
                    print(f"'its close, {args}'")


xxx ()