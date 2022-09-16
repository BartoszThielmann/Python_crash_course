def open_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'File {filename} not found!')
    else:
        print(contents)

open_file('cats.txt')
open_file('dogs.txt')
