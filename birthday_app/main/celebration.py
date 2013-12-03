from datetime import date

class Celebration(object):
    def __init__(self, day, status=None):
        if type(day) is date:
            self.date = day
        else:
            raise TypeError('Day argument must be of type date.')
        
        if status:
            self.status = status
        else:
            self.status='upcoming'
    
    def __repr__(self):
        return self.date.year