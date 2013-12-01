import sys
sys.path.append('')

from birthday_app.main import birthday
import unittest

class test_name_attr(unittest.TestCase):
    def test_default(self):
        birthday_ = birthday.birthday()
        self.assertEqual(birthday_.first_name, None)
    
    def test_kwarg(self):
        first_name = 'Frank'
        birthday_ = birthday.birthday(first_name=first_name)
        self.assertEqual(birthday_.first_name, first_name)
        
if __name__ == '__main__':
        unittest.main()