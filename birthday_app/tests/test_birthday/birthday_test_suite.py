import sys
sys.path.append('')

import unittest
from birthday_app.tests.test_birthday.test_first_name import test_name_attr
from birthday_app.tests.test_birthday.test_last_name import test_last_name
from birthday_app.tests.test_birthday import test_birthday_attr
from birthday_app.tests.test_birthday import test_other_names

ALL_TESTS=[
    test_name_attr,
    test_last_name,
    test_birthday_attr.TestBirthdayAttr,
    test_other_names.TestOtherNames
    ]

def suite():
    suite = unittest.TestSuite()
    for test in ALL_TESTS:
            for method in dir(test):
                    if method.startswith('test'):
                            suite.addTest(test(method))
    return suite

if __name__ == '__main__':
    test_runner = unittest.TextTestRunner()
    test_suite = suite()
    test_runner.run(test_suite)