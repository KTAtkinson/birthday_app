import sys
sys.path.append('')

import datetime
import unittest
from birthday_app.json_tools.tools import encoder
from birthday_app.json_tools.tools import decoder
from birthday_app.json_tools.tools import parse_decoded_json

class TestEncodeDecodePyObj(unittest.TestCase):
  def testEncodeDecodeDate(self):
    date = datetime.date(2013, 12, 20)
    encoded_date = encoder.EncodeJson().encode(date)
    decoded_date = decoder.JsonDecoder().decode(encoded_date)
    date_obj = parse_decoded_json.assemble_obj_attrs(decoded_date)
    
    self.assertEqual(date_obj, date)
    

if __name__ == '__main__':
  unittest.main()