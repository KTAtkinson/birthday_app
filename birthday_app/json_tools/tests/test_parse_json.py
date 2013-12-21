"""Testing parse JSON function."""

import sys
sys.path.append('')

import unittest
import json
from birthday_app.json_tools.tools import parse_json

class ParseJsonTest(unittest.TestCase):
  def testParseMultipleObjs(self):
    json_obj_0 = '{name:katie}'
    json_obj_1 = '{name:brian}'
    
    json_string = json_obj_0 + json_obj_1
    json_objs_list = parse_json.parse(json_string)

    self.assertNotEqual(
        json_objs_list,
        [],
        'Parsed string did not contain any complete json strings.')
    
    self.assertEqual(json_objs_list[0], 
                    json_obj_0, 
                    make_err('First', json_objs_list[0], json_obj_0))
    self.assertEqual(json_objs_list[1], 
                    json_obj_1,
                    make_err('Last', json_objs_list[1], json_obj_1))

  def testComplexjson(self):
    json_string = '{name:Katie, dict:{key1:value1,key2:value2}}'
    
    json_objs_list = parse_json.parse(json_string)
    
    self.assertEqual(json_objs_list[0], json_string,
                      make_err('', json_objs_list[0], json_string))

def make_err(place, obj, refer):
  return '{0} item was {1}, not {2}.'.format(place, obj, refer)

if __name__ == "__main__":
  unittest.main()