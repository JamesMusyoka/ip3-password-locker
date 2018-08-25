from accounts import Accounts

def create_accounts(fname, lname, email, username, password):
    '''
    This function creates a new account.
    '''
    new_accounts = Accounts(fname, lname, email, username, password)
    return new_accounts

def save_accounts(accounts):
    '''
    This function saves an account.
    '''
    accounts.save_accounts()

def del_accounts(accounts):
    '''
    This function deletes an account.
    '''
    accounts.delete_accounts()

def display_accounts():
    '''
    This function returns all the saved accounts.
    '''
    return Accounts.display_accounts()
