class Error(Exception):
        def __init__(self, arg):
                self.arg = arg
        
        def __str__(self):
                return repr(
                    '{self.arg} is not a valid kwarg for this type.'.format(
                        self=self))
                    