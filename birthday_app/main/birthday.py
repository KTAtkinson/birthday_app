import sys
sys.path.append('')

import datetime
from birthday_app.errors import unsupported_kwarg
from birthday_app.main.celebration import Celebration
import string
import random

class birthday(object):
    def __init__(self, birthdate=None, 
                  first_name=None, 
                  last_name=None, 
                  other_names=None, 
                  id=None):
        
        if type(birthdate) is datetime.date:
            self.birthday = birthdate
        elif not birthdate:
            self.birthday = datetime.date.today()
        else:
            raise TypeError('birthday arg must be of the type date or equal None.')
        
        self.first_name = first_name
        self.last_name = last_name
        
        if type(other_names) is list:
            self.other_names = other_names
        elif other_names is None:
            self.other_names = []
        else:
            raise TypeError()
        
        self.id = id
        self.celebrated = []
    
    def add_celetration(self, date):
        self.celebrated = Celebration(date)