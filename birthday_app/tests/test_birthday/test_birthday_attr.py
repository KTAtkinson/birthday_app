import sys
sys.path.append('')

import unittest
from datetime import date
from birthday_app.main import birthday

class TestBirthdayAttr(unittest.TestCase):
    def test_default(self):
        foo = birthday.birthday()
        self.assertEqual(foo.birthday, date.today())
      
    def test_set_birthday(self):
        day = 22
        month = 10
        year = 1988
        birthdate = date(year, month, day)
        print type(birthdate)
        
        foo = birthday.birthday(birthdate=birthdate)
        self.assertEqual(foo.birthday, birthdate)
    
    def test_type_error(self):
        self.assertRaises(TypeError, birthday.birthday, kwds={'birthdate':5})

if __name__ == '__main__':
    unittest.main()
