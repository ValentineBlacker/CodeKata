import unittest
import datetime
from babysitter import Babysit

class testBabysitter(unittest.TestCase):
    """
    A test class for the Babysitter module
    """

    def setUp(self):
        #init babysitter class
        self.babysitter = Babysit()

    def testStartTime(self):
        #can't start too early
        self.assertTrue(Babysit.check_start_time(self.babysitter, datetime.time(17,00)))
        self.assertTrue(Babysit.check_start_time(self.babysitter, datetime.time(04,00)))
        self.assertFalse (Babysit.check_start_time(self.babysitter, datetime.time(16,59)))
        self.assertFalse (Babysit.check_start_time(self.babysitter, datetime.time(04,01)))

    def testEndTime(self):
        #can't work too late
        self.assertTrue(Babysit.check_start_time(self.babysitter, datetime.time(04,00)))
        self.assertTrue(Babysit.check_start_time(self.babysitter, datetime.time(17,00)))
        self.assertFalse(Babysit.check_start_time(self.babysitter, datetime.time(04,01)))
        self.assertFalse(Babysit.check_start_time(self.babysitter, datetime.time(16,59)))
        

if __name__ == '__main__':
    unittest.main()
    
