class account:
    '''
    Class that generates details of accounts
    '''

    acount_list = []

    def __init__(self,account,user_name,email_address,password):

        self.acount = account
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
