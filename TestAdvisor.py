import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor

class TestAdvisor(unittest.TestCase) :    

    def setUp(self):
        self.prepresources1 = Advisor.populatePrepResources(1)
        self.prepresources2 = Advisor.populatePrepResources(2)        
        self.oresources1 = Advisor.populateOLResources(1)
        self.oresources2 = Advisor.populateOLResources(2)
        
    def test_populatePrepResources(self):
        self.assertIn('Knowledge Test',self.prepresources1.resources[0][0])
        self.assertIn('Get-your-L.aspx',self.prepresources1.resources[0][1])
        self.assertIn('RoadTest 7',self.prepresources2.resources[0][0])
        self.assertIn('Get-your-N.aspx',self.prepresources2.resources[0][1])
        
    def test_populateOLResources(self):
        self.assertIn("Book a ICBC Knowledge",self.oresources1.resources[0][0])
        self.assertIn("maticwebbookin",self.oresources1.resources[0][1])
        self.assertIn("Book a Road Test 7",self.oresources2.resources[0][0])
        self.assertIn("webdeas-ui",self.oresources2.resources[0][1])

    def tearDown(self):
        del(self.prepresources1)
        del(self.prepresources2)
        del(self.oresources1)
        del(self.oresources2)
        
