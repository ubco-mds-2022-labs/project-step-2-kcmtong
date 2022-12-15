import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor, Resource

## TODO (Nowshaba) : Follow the template and fill in the remaining
class TestResource(unittest.TestCase) :    

    def setUp(self):
        self.pr1 =  Resource.PrepResource(1,[['Prep Stage ONE','http://pstageone.com']])
        self.or1 =  Resource.OLResource(1,[['OL Stage ONE','http://ostageone.com']])
        ## TODO (Nowshaba) : continue for self.pr2, self.or2
        
    def test_createPrepResource(self):
        self.assertIn('Prep Stage',self.pr1.resources[0][0])
        self.assertIn('pstageone.com',self.pr1.resources[0][1])
        ## TODO (Nowshaba) : continue for self.pr2

    def test_createOLResource(self):
        self.assertIn('OL Stage',self.or1.resources[0][0])
        self.assertIn('ostageone.com',self.or1.resources[0][1])
        ## TODO (Nowshaba) : continue for self.or2

    def tearDown(self):
        del(self.pr1)
        del(self.or1)
        ## TODO (Nowshaba) : continue for self.pr2/or2