print('Please provide two numbers to add')
while True:
    try:
        num1 = int(input('First number: '))
        num2 = int(input('Second number: '))
    except ValueError:
        print("Can't add strings! You need to pass a integer!")
    else:
        break
print('The sum is ' + str(num1+num2))
