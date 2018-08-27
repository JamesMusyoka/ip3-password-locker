from user import User
from credentials import Credentials
import pyperclip

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

def check_existing_user(email):
    '''
    This function checks if a user exists with that email and returns a Boolean.
    '''

def main():
    print("Hello, welcome to your user list. What is your name?")

    user_name = input()
    print("")

    print("Hello {user_name}. What would you like to do?")
    print("\n")

    while True:
            print("Use these short codes : ca - create new user, dc - display users, fa - find user, ex - exit ")

            short_code = input().lower()

            if short_code == 'ca':
                    print("New User")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Username ...")
                    u_name = input()

                    print("Email address ...")
                    e_address = input()


                    save_user(create_user())
                    print ('\n')
                    print("New User {f_name} {l_name} created")
                    print ('\n')

            elif short_code == 'da':

                    if display_user():
                            print("Here is a list of all your users")
                            print('\n')

                            for user in display_user():
                                    print("{user.first_name} {user.last_name} .....{user.username}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any users saved yet")
                            print('\n')

            elif short_code == 'fa':

                    print("Enter the email you want to search for")

                    search_email = input()
                    if check_existing_user(search_email):
                            search_user = find_user(search_email)
                            print("{search_user.first_name} {search_user.last_name}")
                            print('-' * 20)

                            print("Username.......{search_user.username}")
                            print("Email address.......{search_user.email}")
                    else:
                            print("That user does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
