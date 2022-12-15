import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor

class TestUserProfile(unittest.TestCase) :    

#    def setUpClass(cls):
#        print('setupclass')
    
    def setUp(self):
        self.p1 =  UserProfile.UserProfile('Kenny',0,False,False,1)
        self.p2 =  UserProfile.UserProfile('John',1,True,True,1)
        
    def test_createProfile(self):
        self.assertEqual(self.p1.name,'Kenny')
        self.assertFalse(self.p1.current_icbc_lic)
        self.assertEqual(self.p2.name,'John')
        self.assertTrue(self.p2.current_icbc_lic)

    def test_str(self):
        self.assertIn('None',str(self.p1))
        self.assertIn('No',str(self.p1))
        self.assertIn('Learner',str(self.p2))
        self.assertIn('Yes',str(self.p2))
        
    def tearDown(self):
        del(self.p1)
        del(self.p2)
        