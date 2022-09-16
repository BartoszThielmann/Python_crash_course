while True:
    name = input('Plase state your name: ')
    print(f'Hello, {name}')
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(name + '\n')
