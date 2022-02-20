import getpass # for hiding the password while typing
from instaScraper import Scraper 

if __name__ == '__main__':

    print('Enter the username and password of your Instagram Account')
    #username = input('Username: ') # input your username
    username = 'username'
    #password = getpass.getpass() # input your password
    password = 'password'
    print('Enter the username of the target whose photos and descriptions you want to download from')
    '''
        target_username must fulfill either or both of the below two criteria:
        -> You must follow that account
        -> It must be an open account.
    '''
    #target_username = input('Target Username: ') # Enter the username of the account you want to scrap photos and capions from.
    
    target_username = 'target_username'

    scraper = Scraper(username, password, target_username) # Instagram Scraper Object