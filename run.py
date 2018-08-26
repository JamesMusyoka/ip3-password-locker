from user import User

def create_user(fname, lname, email, username, password):
    '''
    This function creates a new account.
    '''
    new_user = User(fname, lname, email, username, password)
    return new_user

def save_user(user):
    '''
    This function saves an account.
    '''
    user.save_user()

def del_user(user):
    '''
    This function deletes an account.
    '''
    user.delete_user()

def display_user():
    '''
    This function returns all the saved user.
    '''
    return User.display_user()
