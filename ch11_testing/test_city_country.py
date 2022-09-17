import unittest
from city_functions import cc_formatting

class CitiesTestCase(unittest.TestCase):
    """Tests city_functions.py"""
    
    def test_city_country_formatting(self):
        """Does the city and country name formatting work"""
        formatted = cc_formatting('santiago','chile')
        self.assertEqual(formatted, 'Santiago, Chile')
        
    def test_city_country_population_formatting(self):
        """Does the city, country and population formatting work"""
        formatted = cc_formatting('santiago','chile', population=50000000)
        self.assertEqual(formatted, 'Santiago, Chile, population - 50000000')
        
if __name__ == '__main__':
    unittest.main()
