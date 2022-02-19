import unittest
from credentials import Credential
from user import User

class TestCredentials(unittest.TestCase):
    def setUp(self):
        
        #create a credential object test 
        self.new_credential = Credential("Isaac", "havertz", "twitter", "Uy67tye")
       
    def tearDown(self):
        Credential.credential_list=[]
        
    def test_init(self):
        '''
        Testcase to test of the credential object is properly initialized 
        '''
        self.assertEqual(self.new_credential.user_name, "Isaac")
        self.assertEqual(self.new_credential.user_password, "havertz")
        self.assertEqual(self.new_credential.credential_name, "twitter")
        self.assertEqual(self.new_credential.credential_password, "Uy67tye")
        
        