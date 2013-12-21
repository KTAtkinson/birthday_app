import sys
sys.path.append('')

import json
import datetime
import unittest
from birthday_app.json_tools.tools import encoder
from birthday_app.json_tools.tools import encode_date

class TestEncoder(unittest.TestCase):
  def testEncodeBuiltIn(self):
    py_list = ['nothing']
    encoded_list = encoder.EncodeJson().encode(py_list)
    self.assertEqual(encoded_list, json.dumps(py_list))
  
  def testObjHook(self):
    py_date = datetime.date(1988, 10, 22)
    encoded_date = encoder.EncodeJson().encode(
        py_date)
    
    mock_json = (
        """{"__module__": "datetime", "month": 10, """ +
        """"year": 1988, "__class__": "date", "day": 22}""")
    self.assertEqual(encoded_date, mock_json)

  def testEncodeDictWithDateValue(self):
    py_dict = {'date' : datetime.date(2013, 12, 20)}
    encoded_dict = encoder.EncodeJson().encode(py_dict)
    
    expected_json = ('''{"date": {"__module__": "datetime", "month": 12, ''' +
        '''"year": 2013, "__class__": "date", "day": 20}}''')
    self.assertEqual(encoded_dict, expected_json)
    

if __name__ == '__main__':
  unittest.main()