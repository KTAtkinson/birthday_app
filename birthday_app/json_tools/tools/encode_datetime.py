"""Encode datetime object into a JSON string"""

import sys
sys.path.append('')

import json

class Encode(json.JSONEncoder):
  def default(self, obj):
    attr_dict = dict()
    attr_dict['year'] = obj.year
    attr_dict['month'] = obj.month
    attr_dict['day'] = obj.day
    
    attr_dict['__class__'] = obj.__class__
    
    return attr_dict


if __name__ == '__main__':  
  pass