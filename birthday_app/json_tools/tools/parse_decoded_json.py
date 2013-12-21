import sys
sys.path.append('')

from birthday_app.json_tools.tools import decoder
from birthday_app.json_tools.tools import parse_json

def assemble_obj_attrs(decoded_json):
  obj_dict = decoded_json
  
  if type(decoded_json) is str:
    if value[0] == '{':
      json_string = parse_json.parse(value)
      return decoder.JsonDecoder().decode(json_string)
  
  if is_iter(decoded_json):
    return parse_iter(value)
  
  return decoded_json

def parse_iter(_iter):
  if type(_iter) is dict:
    new_obj = dict()
    if "__class__" in _iter.keys():
      return decoder.JsonDecoder().deocode(_iter)
    for i, value in _iter:
      if type(value) is dict and "__class__" in _iter.keys():
        new_obj[i] = build(value)
      elif is_iter(value):
        new_obj[i] = parse_iter(value)
      else:
        new_obj[i] = value
  
  elif type(_iter) is list:
    new_obj = list()
    for value in _iter:
      if is_iter(i):
        new_obj.append(parse_iter(_iter))
      else:
        new_obj.append(_iter)
  
  return new_obj

def is_iter(value):
  try:
    value.__iter__
  except AttributeError:
    return False
  else:
    return True

