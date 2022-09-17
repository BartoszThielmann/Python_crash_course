class Employee:
    """A class representing an employee"""
    
    def __init__(self, fname, lname, salary):
        """Initiate first name, last name and annual salary"""
        self.fname = fname
        self.lname = lname
        self.salary = salary
        
    def give_raise(self, sraise=5000):
        self.salary += sraise
