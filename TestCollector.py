import unittest
from DLAdvisor.ProfileBuilder import Collector, UserProfile
from DLAdvisor.Analyzer import Advisor

class TestCollector(unittest.TestCase) :    

    def setUp(self):
        pass
        
    def test_greeting(self):
        # The greeting() method in the Collector contains message printing, but without and return string
        # No testing can therefore be done here.
        pass
    
    def test_passBasicEligibility(self):
        # The passBasicEligibility() method in the Collector are mainly interactive functions which ask for ouser input and then perform validation, which can not be automated easily.  
        # Manual testing can be done to ensure the proper user interaction behaviour.
        pass
    
    def tearDown(self):
        pass

