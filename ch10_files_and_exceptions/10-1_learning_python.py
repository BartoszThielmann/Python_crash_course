with open('10-1_learning_python.txt') as file_object:
    content = file_object.read()
print(content)

with open('10-1_learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
    print('')
        
with open('10-1_learning_python.txt') as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
