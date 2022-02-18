import string 
from random import choice
'''
import string and random modules into the file
'''
class Credential:
    '''
    class blueprint to creat instances of credentials
    '''
    
    credential_list = []
    def __init__(self, user_name, user_password, credential_name, credential_password):
        
        '''
        Args:
            user_name: name of the user
            user_password: user login password
            credential_name: user account's name 
            credential_password: user account's password
        '''
     def save_credential(self):
        Credential.credential_list.append(self)
        
    @classmethod
    def generate_password(cls):
        '''
        method to generate a random passcode
        '''
        size=6
        
        passcode=string.ascii_uppercase+string.digits+string.ascii_uppercase
        
        #creating the login password
        password=''.join(choice(passcode) for num in range(size))
        
        return password
        
        
        
    