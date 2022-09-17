import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee.py"""
    
    def setUp(self):
        """Create Employee instance"""
        self.some_employee = Employee('Bartosz', 'Thielmann', 8000)
        
    def test_give_default_raise(self):
        self.some_employee.give_raise()
        self.assertEqual(13000, self.some_employee.salary)
    
    def test_give_custom_raise(self):
        self.some_employee.give_raise(10000)
        self.assertEqual(18000, self.some_employee.salary)
        
if __name__ == '__main__':
    unittest.main()
