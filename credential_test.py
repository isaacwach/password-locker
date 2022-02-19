import unittest
from credentials import Credential
from user import User

class TestCredentials(unittest.TestCase):
    def setUp(self):
        
        #create a credential object test 
        self.new_credential = Credential("Isaac", "havertz", "twitter", "Uy67tye")
        
        