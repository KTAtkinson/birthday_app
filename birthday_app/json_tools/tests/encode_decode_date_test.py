import sys
sys.path.append('')

import datetime
import json
import unittest
from birthday_app.json_tools.tools import make_date_dict
from birthday_app.json_tools.tools import decoder

class EncodeDecodeDateTest(unittest.TestCase):
  def testEncoding(self):
    day = datetime.date(1988, 10, 22)
    encoded_day = make_date_dict.Encode().encode(day)
    decoded_day = decoder.JsonDecoder().decode(encoded_day)
    self.assertEqual(day, decoded_day)
    
  
if __name__ == '__main__':
  unittest.main()