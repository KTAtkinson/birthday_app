import sys
sys.path.append('')

import unittest
from birthday_app.main import birthday

class TestOtherNames(unittest.TestCase):
    def test_default(self):
        new_birthday = birthday.birthday()
        self.assertEqual(new_birthday.other_names, [])
    
    def test_set_other_names(self):
        other_names = ['Fred', 'Joe']
        new_birthday = birthday.birthday(other_names=other_names)
        self.assertEqual(new_birthday.other_names, other_names)
    
    def test_type_error(self):
        self.assertRaises(TypeError, birthday.birthday, kwds={'other_names':'Mike'})
    

if __name__ == '__main__':
    unittest.main()