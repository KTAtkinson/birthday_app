import sys
sys.path.append('')

import json

class JsonDecoder(json.JSONDecoder):
  def __init__(self):
    json.JSONDecoder.__init__(self, object_hook=self.object_to_dict)
  
  def object_to_dict(self, attr_dict):
    if "__class__" in attr_dict:
      class_name = attr_dict.pop('__class__')
      module_name = attr_dict.pop('__module__')
      module = __import__(module_name)
      class_ = getattr(module, class_name)
      
      args = dict((key.encode('ascii'), value) for key, value in attr_dict.items())
      inst = class_(**args)
    else:
      inst = attr_dict
    
    return inst
      
  
    