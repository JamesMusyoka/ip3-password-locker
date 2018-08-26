from user import User
from credentials import Credentials

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

def delete_user(user):
    '''
    This function deletes an account.
    '''
    user.delete_user()

def display_user():
    '''
    This function returns all the saved user.
    '''
    return User.display_user()

def find_user(email):
    '''
    This function finds a user by their email address.
    '''
    return User.find_by_email(email)

def main():
    print("Hello, welcome to your accounts list. What is your name?")

        accounts_list = input()

        print(f"Hello {user_name}. What would you like to do?)
        print('\n')

        while true:
            print("Use these short codes : ca - create new account, dc - display accounts, fa - find account, ex - exit ")

            short_code = input().lower()

                    if short_code == 'ca':
                            print("New Account")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Username ...")
                            u_name = input()

                            print("Email address ...")
                            e_address = input()


                            save_accounts(create_account(f_name,l_name,u_name,e_address))
                            print ('\n')
                            print(f"New Account {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'da':

                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.username}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'fa':

                            print("Enter the email you want to search for")

                            search_email = input()
                            if check_existing_contacts(search_email):
                                    search_contact = find_contact(search_email)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Username.......{search_account.username}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__'

    main()
