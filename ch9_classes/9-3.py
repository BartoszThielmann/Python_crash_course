class User:
    """User profile"""
    
    def __init__(self, fname, lname, age, city, hobby):
        """Initialize attributes"""
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.city = city
        self.hobby = hobby
        self.login_attempts = 0
    
    def describe_user(self):
        """Print a summary of user information"""
        summary = f'''
        Name: {self.first_name}
        Last name: {self.last_name}
        Age: {self.age}
        City: {self.city}
        Hobby: {self.hobby}
        Login attempts: {self.login_attempts} '''
        print('User description:'+ summary.title())
    
    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}!')
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):
    """Class representing a admin"""
    
    def __init__(self, fname, lname, age, city, hobby):
        """Initialize user attributes and then Admin attributes"""
        super().__init__(fname, lname, age, city, hobby)
        self.privileges = ['can add post','can delete post', 'can ban user']
        
    def show_privileges(self):
        """Shows admin privileges"""
        print(f'{self.first_name} {self.last_name} privileges are:')
        for privilege in self.privileges:
            print(privilege, end=' | ')

user1 = User('Bartosz', 'Thielmann', 23, 'Wroclaw', 'martial arts')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
user1.greet_user()
user1.reset_login_attempts()
user1.describe_user()

user2 = Admin('Marika', 'Halonko', 26, 'Wroclaw', 'pets')
user2.show_privileges()
