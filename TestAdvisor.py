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
        self.assertIn('Learn stage 1',self.prepresources1.resources[0][0])
        self.assertIn('stage1.com',self.prepresources1.resources[0][1])
        self.assertIn('Learn stage 2',self.prepresources2.resources[0][0])
        self.assertIn('stage2.com',self.prepresources2.resources[0][1])
        
    def test_populateOLResources(self):
        self.assertIn("Test OL",self.oresources1.resources[0][0])
        self.assertIn("stage1.com",self.oresources1.resources[0][1])
        self.assertIn("RoadTest7 OL",self.oresources2.resources[0][0])
        self.assertIn("stage2.com",self.oresources2.resources[0][1])

    def tearDown(self):
        del(self.prepresources1)
        del(self.prepresources2)
        del(self.oresources1)
        del(self.oresources2)
        
