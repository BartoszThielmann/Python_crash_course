import json

def get_stored_number():
    """Gets user's stored favorite number"""
    try:
        with open('fav_num.json') as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def report_fav_number():
    """If the favorite number is already stored it provides it to the user"""
    fav_num = get_stored_number()
    if fav_num:
        print(f'Your favorite number is {fav_num}')
    else:
        get_fav_number()
    
        
def get_fav_number():
    """Asks user for his favorite number and saves it"""
    fav_num = input("What's your favorite number? ")
    with open('fav_num.json', 'w') as f:
        json.dump(fav_num, f)
    print('Your favorite number is saved')

report_fav_number()
