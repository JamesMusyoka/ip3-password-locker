class Credentials:
    '''
    Class that generates new instances of credentials.
    '''

    credentials_list = []

    def __init__(self, username, password):
        '''
        This method helps us define properties for our objects.
        '''

        self.username = username
        self.password = password
