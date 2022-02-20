from user import User
from credentials import Credential

def create_user(username, password):
    new_user=User(username, password)
    return new_user

def save_user(user):
    '''
    method to save a user account 
    '''
    user.save_user()
    
def check_existing_users(name):
    
    return User.user_exists(name)

def user_log_in(name, passcode):
    
    '''
    Args: 
    name: user account username 
    passcode: user account password 
    '''
    log_in=User.log_in(name, passcode)
    if log_in !=False:
        return User.log_in(name, passcode)
    
def display_users():
    '''
    Method that returns all saved users at a given point in time 
    '''
    return User.display_user()

def create_credential(passcode, name, password):
    
    new_credential = Credential(passcode, name, password)
    return new_credential

def save_credentials(credential):
    credential.save_credential()

def check_existing_credential(name):
    return Credential.credential_exist(name)

def display_credentials(password):
    return Credential.display_credentials(password)

def create_generated_password(name):
    
    password=Credential.generate_password()
    return password

def main():
    '''
    Function to run the accounts safe
    '''
    print('''welcome to password locker app \n
          Use these short codes to navigate through the app.''')
    
    while True:
        
        print('''  Short codes:
              ca-creates a user account \n
              du-displays names of current account and users \n
              lg-to log in to your account \n
              q-quit from the account safe account ''')
        
        #take users short codes inputs
        short_codes =input().lower()
        
        if short_codes =="ca":
            print("User name...")  
            username=input()
            
            print("password") 
            password=input() 
            
            save_user(create_user(username,password))
            
            print("\n")
            print(f"{username} welcome to password locker")
            print("\n")
            
        elif short_codes =="du":
            '''
            Display the names of current users 
            '''
            
            if display_users():
                print("\n")
                print("These are the current registred uders")
                print("-"*10)
                
                for user in display_users():
                    print(f"{user.username}")
                    print("-"*10)
                    
            else:
                print("\n")
                print("Password locker has no existing users, be the first user")
                print("\n")
                
        
    
if __name__ == '__main__':
    main()
    
    
    
    