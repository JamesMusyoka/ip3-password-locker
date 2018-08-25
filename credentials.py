class Credentials:
    '''
    Class that generates new instances of credentials.
    '''

    credentials_list = []

    def __init__(self, account, username, password):
        '''
        This method helps us define properties for our objects.
        '''

        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        This methods saves credential objects into the credentials_list.
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        This method deletes saved credentials from the credentials_list.
        '''
        
        Credentials.credentials_list.remove(self)
