import sys
sys.path.append('')


def is_magic(string):
  if type(string) is not str:
    raise TypeError('expected a string, got {}.'.format(type(string).__name__))
  
  try:
    string[1]
  except IndexError:
    return False
  else:
    pass
  
  if string[:2] == "__" and string[-2:] == "__":
    return True
  
  return False
  