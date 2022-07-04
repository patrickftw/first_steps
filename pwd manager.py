def view():
    pass

def add():
    name = input('Nazwa uzytkownika: ')
    pwd = input('Haslo: ')

    file = open('passwords.txt', 'a')
    file.write(name + "|" + pwd)
    file.close()


while True:
    mode = input('Would you like to add new password or view existing ones? (view, add, q to quit) ')
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
