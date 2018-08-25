import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    This is a test subclass that defines cases for the credentials class behaviour.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

def test_init(self):
    '''
    This test tests if an object is initialised properly.
    '''

    self.assertEqual(self.new_credentials.account,"Gmail")
    self.assertEqual(self.new_credentials.username,"nanciekathini")
    self.assertEqual(self.new_credentials.password,"12ab")


if __name__ == '__main__':
