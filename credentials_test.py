import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    '''
    This is a test subclass that defines cases for the credentials class behaviour.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''

def tearDown(self):
    '''
    This method does clean up after each test has run.
    '''
    Credentials.credentials_list = []

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_credentials = Credentials("Nancy", "Muthinzi", "nanciekathini@gmail.com")


def test_init(self):
    '''
    This test tests if an object is initialized properly.
    '''

    self.assertEqual(self.new_credentials.account,"Gmail")
    self.assertEqual(self.new_credentials.username,"nanciekathini")
    self.assertEqual(self.new_credentials.password,"12ab")

def test_save_credentials(self):
    '''
    This is to test if the credentials objects are saved into the credentials_list.
    '''
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()
