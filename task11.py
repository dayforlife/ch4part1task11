def error_decor(func):
    def wrapper(*args, **kwargs):
        print(func())
        if func() == True:
            raise Exception('No username defined!')
        elif func() == False:
            raise Exception("No password to change!")
    return wrapper

def get_return(func):
    def wrapper():
        if func() == 'account':
            return True
        elif func() == 'password':
            return False 
    return wrapper

class User():
    @error_decor
    @get_return
    def get_account_balance():
        return 'account'

    @error_decor
    @get_return
    def change_password():
        return 'password'

user = User()
# print(user.get_account_balance()) 
print(user.change_password())
