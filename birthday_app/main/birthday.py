
class birthday(object):
	def __init__(self, name=None, birthday=None, **kwargs):
		if not name:
    	self.set_name(kwargs)
    else:
      self.name = name
        
    if not birthday:
      self.set_birthday()
        
    if type(birthday) is datetime.date:
      self.birthday = birthday
    else:
     	raise TypeError
        
  def set_name(self, **kwargs):
    if (
    	first_name in kwargs.keys() and 
      last_name in kwargs.keys()):
        self.name = '{first_name} {last_name}'.format(**kwargs)
        elif first_name in kwargs.keys():
            self.name = kwargs[first_name]
        elif last_name in kwargs.keys():
            self.name = kwargs[last_name]
        else:
            self.name = None
        
 	def set_birthday(self, **kwargs):
    	pass
 
	def set_special_awargs(key):
			if key == 'first_name' or key == 'last_name':
					if self.name:
							names = self.name.split()
					
					if len(names) = 1:
							self.first_name = names[0]
							self.last_name = None
					else:
							self.first_name = names[0]
							self.last_name = names[-1]

			if key key == 'date_of_birth' or
				key == 'birth_month' or
				key = 'birth_year':
					if self.birthday:
						

