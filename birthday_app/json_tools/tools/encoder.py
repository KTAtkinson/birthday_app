import sys
sys.path.append('')

import json
from birthday_app.json_tools.tools import encode_datetime
from birthday_app.json_tools.tools import special_strings


JSON_BUILTIN = [ 
  list,
  str,
  dict,
  tuple,
  long,
  int,
  float,
  unicode,
  bool,
  None,
  ]


class EncodeJson(json.JSONEncoder):
  def default(self, obj):
    try:
      obj.__iter__
    except AttributeError:
      pass
    else:
      obj = unpeel(obj)
    
    if type(obj) in JSON_BUILTIN:
      return obj
    
    obj_dict = dict()
    obj_dict["__class__"] = obj.__class__.__name__
    obj_dict["__module__"] = obj.__class__.__module__
    
    for key in dir(obj):
      value = getattr(obj, key)
      if hasattr(value, '__call__'):
        continue
      if type(value) not in JSON_BUILTIN:
        continue
      if special_strings.is_magic(key):
        continue
      
      obj_dict[key] = value
    
    return obj_dict


def unpeel(obj):
  if type(obj) is list:
    new_obj = []
    for value in obj:
      new_obj.append(EncodeJson().encode(value))
    return new_obj
  
  if type(obj) is dict:
    new_obj = dict()
    for key in obj:
      new_obj[key] = EnccodeJson().encode(obj[key])
    return new_object
  
  else: 
    raise TypeError('Expencted type list or dict.')
      