import unittest
from datetime import time
from babysitter import Babysit

class testBabysitter(unittest.TestCase):
    """
    A test class for the Babysitter module
    I assumed that the babysitter could work for 0 minutes (but get paid $0 for it),
    and that the kids had to be in bed by midnight, which is reasonable.
    """

    #TODO: make sure end time is not before bedtime, bedtime not before start time
    
    def setUp(self):
        #init babysitter class
        self.babysitter = Babysit()

    def test_StartTime(self):
        #can't start too early
        self.assertTrue(Babysit.check_start_time(self.babysitter, time(17,00)))
        self.assertTrue(Babysit.check_start_time(self.babysitter, time(04,00)))        
        self.assertFalse (Babysit.check_start_time(self.babysitter, time(16,59)))
        self.assertFalse (Babysit.check_start_time(self.babysitter, time(04,01)))        

    def test_EndTime(self):
        #can't work too late
        self.assertTrue(Babysit.check_end_time(self.babysitter, time(04,00)))
        self.assertTrue(Babysit.check_end_time(self.babysitter, time(17,00)))
        self.assertFalse(Babysit.check_end_time(self.babysitter, time(04,01)))
        self.assertFalse(Babysit.check_end_time(self.babysitter, time(16,59)))        

    def test_BedTime(self):
        #kids need to be in bed before midnight, but after we've started sitting
        self.assertTrue(Babysit.check_bed_time(self.babysitter, time(23,59)))
        self.assertTrue(Babysit.check_bed_time(self.babysitter, time(17,00)))
        self.assertFalse(Babysit.check_bed_time(self.babysitter, time(00,01)))
        self.assertFalse(Babysit.check_bed_time(self.babysitter, time(04,59)))

    def test_HoursPaidFromStartToBed(self):
        #make sure babysitter gets paid $12/hr from start to bedtime
        self.assertEqual(36, Babysit.pay_start_to_bed(self.babysitter, time(17,00),time(20,00)))
        self.assertEqual(12, Babysit.pay_start_to_bed(self.babysitter, time(17,00), time(17,01)))
        self.assertEqual(12, Babysit.pay_start_to_bed(self.babysitter, time(23,00), time(00,00)))

    def test_HoursPaidFromBedToMid(self):
        #get paid $8 between when the kids go to bed and midnight.
        #partial hours are paid at higher $12 rate
        #must calculate case where end time is before midnight
        self.assertEqual(8, Babysit.pay_bed_to_mid(self.babysitter, time(22,30), time (01,00)))
        self.assertEqual(16, Babysit.pay_bed_to_mid(self.babysitter, time(22,00),time(00,00)))
        self.assertEqual(16, Babysit.pay_bed_to_mid(self.babysitter, time(17,30),time(20,00)))
        self.assertEqual(24, Babysit.pay_bed_to_mid(self.babysitter, time(17,30),time(20,30)))

    def test_HoursPaidFromMidToEnd(self):
        #if end time is after midnight, pay $16 an hour from midnight to end.
        #partial hours count as full.
        self.assertEqual(0, Babysit.pay_mid_to_end(self.babysitter, time(23,30)))
        self.assertEqual(32, Babysit.pay_mid_to_end(self.babysitter, time(01,30)))

    def test_TotalPay(self):
        #calculate total pay using previous methods
        self.assertEqual(120, Babysit.calculate_total(self.babysitter, time(19,30), time(22,30), time(3,30)))
        self.assertEqual(64, Babysit.calculate_total(self.babysitter, time(17,25), time(18,30), time(23,30)))

if __name__ == '__main__':
    unittest.main()
    
