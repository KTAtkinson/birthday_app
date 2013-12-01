import sys
sys.path.append('')

from datetime import date
from birthday_app.errors import unsupported_kwarg

class birthday(object):
        def __init__(self, birthday=None, **kwargs):
                if type(birthday) is date:
                        self._set_birthday(birthday)
                if not birthday:
                        self._set_birthday(date.today())
                else:
                        raise TypeError('birthday must be of type datetime.date')
                
                accepted_kwargs = ['first_name', 'last_name', 'other_names']
                
                for attr in kwargs:
                        if attr in accepted_kwargs:
                                self.__setattr__(attr, kwargs[attr])
                        else:
                                raise unsupported_kwarg.Error(self, attr)
                
                for arg in accepted_kwargs:
                        try:
                                self.__getattribute__(arg)
                        except AttributeError:
                                self.__setattr__(arg, None)
                
        def _set_birthday(self, birthday):
                self.birth_date = birthday.day
                self.birth_month = birthday.month
                self.birth_year = birthday.year