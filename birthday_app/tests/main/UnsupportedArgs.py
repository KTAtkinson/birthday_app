class Error(Exception):
    
    def __init__(self, unsupported_attrs):
        self.attrs = unsupported_attrs
    
    def __str__(self):
        return repr(self.make_error())
    
    def make_error(self):
        if len(self.attrs) == 1:
            return 'The following attr is not supported {0}'.format(self.args)
        else:
            error = 'The following attrs are not supported:'
            for attr in self.attrs:
              error += ' {0}'.format(attr)
        return error