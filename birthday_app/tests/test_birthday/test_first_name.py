from birthday_app.main import birthday
import unittest

class test_name_attr(unittest.TestCase):
    def test_default(self):
        birthday.birthday()
        self.assertEqual(self.first_name, None)
    
    def test_kwarg(self):
        first_name = 'Frank'
        birthday.birthday(first_name=first_name)
        self.assertEqual(self.first_name, first_name)