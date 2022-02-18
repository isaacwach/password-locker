from credentials import Credential

class User:
    '''
    create a User class that generates new instances of a user 
    '''
    user_list = []
    
    def __init__(self, username, password):
        '''
        initialization method to define user object properties
        args: 
        username: name of the user 
        password: user's password 
        '''
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        a method to save a new user instance into the user_list 
        '''
        User.user_list.append(self)
        
    @classmethod
    def display_user(cls):
        return cls.user_list 
    
        