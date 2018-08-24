class Accounts:
    '''
    Class that generates details of accounts
    '''

    accounts_list = []

    def __init__(self, first_name, last_name, email_address, username, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.username = username
        self.password = password

    def save_accounts(self):

        '''
        This method saves accounts objects into the accounts_list.
        '''

        Accounts.accounts_list.append(self)
