import sys
sys.path.append('')

import unittest
from birthday_app.tests.test_birthday.test_first_name import test_name_attr
from birthday_app.tests.test_birthday.test_last_name import test_last_name

ALL_TESTS=[
    test_name_attr,
    test_last_name
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