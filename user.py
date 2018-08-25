class User:
    '''
    Class that generates new instances of a user.
    '''

    user_list = []

    def __init__(self, first_name, last_name, email_address, username, password):
        '''
        This method helps us define properties for our objects.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.username = username
        self.password = password

    def save_user(self):

        '''
        This method saves user objects into the user_list.
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        This method deletes a saved user from the user_list.
        '''

        User.user_list.remove(self)
