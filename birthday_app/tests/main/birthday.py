
import UnsupportedArgs
import datetime

class birthday(object):
    TODAY = datetime.date.today()
    def __init__(self, birthday=TODAY, **kwargs):
        self.birth_year = birthday.year
        self.birth_month = birthday.month
        self.birth_date = birthday.day        
        
        all_attrs = [
          'first_name',
          'last_name',
          'other_names']          
        unused_args = []
        
        for attr in kwargs:
            if attr in all_attrs:
                self.__setattr__(attr, kwargs[attr])
            else:
                unused_args.append(attr)
        
        if unused_args:
            raise UnsupportedArgs.Error(unused_args)
        
        for attr in all_attrs:
            try:
                self.__getattribute__(attr)
            except AttributeError:
                self.setUndefinedAttr(attr)
            
                
    def setUndefinedAttr(self, attr):
        birthday_attrs = ['birthday_day', 'birth_month', 'birth_year']
        today = datetime.date.today()
        
        if attr not in birthday_attrs:
            self.__setattr__(attr, None)
        elif attr == 'birth_day':
            self.__setattr__(attr, today.day)
        elif attr == 'birth_month':
            self.__setattr__(attr, today.month)
        elif attr == 'birth_year':
            self.__setattr__(attr, today.year)
    
    def return_birth_month(self):
        months = [
          'January',
          'Febuary',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
        
        return months[self.birth_month-1]
            
if __name__ == '__main__':
    birthday_obj = birthday()
    import pdb; pdb.set_trace()
    
    
    
    
            