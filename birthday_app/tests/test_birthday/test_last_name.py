import sys 
sys.path.append('')

from birthday_app.main import birthday
import unittest

class test_last_name(unittest.TestCase):
    def test_default(self):
        birthday_ = birthday.birthday()
        self.assertEqual(birthday_.last_name, None)
    
    def test_kwarg(self):
        last_name = 'Smith'
        birthday_ = birthday.birthday(last_name=last_name)
        self.assertEqual(birthday_.last_name, last_name)

if __name__ == '__main__':
    unittest.main()