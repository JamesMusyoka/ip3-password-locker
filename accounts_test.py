import unittest
import pyperclip
from accounts import Accounts


class TestAccounts(unittest.TestCase):

    '''
    Test class that defines test cases for the accounts class behaviours.

    Args:
        unittest.TestCase: Test case class that helps in creating test cases.
    '''

    def tearDown(self):
        '''
        This method does clean up after each test has run.
        '''
        Accounts.accounts_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_accounts = Accounts("Nancy", "Muthinzi", "nanciekathini@gmail.com", "nanciekathini", "12ab")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_accounts.first_name, "Nancy")
        self.assertEqual(self.new_accounts.last_name, "Muthinzi")
        self.assertEqual(self.new_accounts.email_address, "nanciekathini@gmail.com")
        self.assertEqual(self.new_accounts.username, "nanciekathini")
        self.assertEqual(self.new_accounts.password, "12ab")

    def test_save_accounts(self):
        '''
        test_save_accounts test case to test if the accounts object is saved into the accounts list.
        '''
        self.new_accounts.save_accounts()
        self.assertEqual(len(Accounts.accounts_list),1)

    # def test_save_multiple_accounts(self):
    #     '''
    #     This is to test if we can save multiple objects to our accounts_list.
    #     '''
    #     self.new_accounts.save_accounts()
    #     test_accounts = Accounts("Test", "user", "nanciekathini@gmail.com", "test@user.com")
    #     test_accounts.save_accounts()
    #     self.assertEqual(len(Accounts.accounts_list),2)

    # def test_delete_accounts(self):
    #     '''
    #     This is to test if we can remove an account from our accounts list.
    #     '''
    #     self.new_accounts.save_accounts()
    #     test_accounts = Accounts("Test", "user", "nanciekathini@gmail.com")
    #     test_accounts.save_accounts()
    #
    #     self.new_accounts.delete_account()
    #     self.assertEqual(len(Accounts.accounts_list),1)
    # 
    # def test_copy_username(self):
    #     '''
    #     Test to confirm that we're copying username from an account.
    #     '''
    #
    #     self.new_accounts.save_accounts()
    #     Accounts.copy_username("nanciekathini")
    #
    #     self.assertEqual(self.new_accounts.username, pyperclip.paste())
    #
    # def test_copy_email_address(self):
    #     '''
    #     Test to confirm that we are copying the email address from an account.
    #     '''
        #
        # self.new_accounts.save.accounts()
        # Accounts.copy_email_address("nanciekathini@gmail.com")
        #
        # self.assertEqual(self.new_account.email_address, pyperclip.paster())


if __name__ == '__main__':
            unittest.main()
