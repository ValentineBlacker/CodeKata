import unittest
from datetime import time
from babysitter import Babysit

class testBabysitter(unittest.TestCase):
    """
    A test class for the Babysitter module
    I assumed that the babysitter could work for 0 minutes (but get paid $0 for it),
    and that the kids had to be in bed by midnight, which is reasonable.
    """
    
    def setUp(self):
        #init babysitter class
        self.babysitter = Babysit()

    def test_StartAndEndTime(self):
        #can't start too early or end too late
        self.assertTrue(Babysit.check_start_or_end_time(self.babysitter, time(17,00)))
        self.assertTrue(Babysit.check_start_or_end_time(self.babysitter, time(04,00)) )      
        self.assertFalse(Babysit.check_start_or_end_time(self.babysitter, time(04,01)))
        self.assertFalse(Babysit.check_start_or_end_time(self.babysitter, time(16,59)) )       

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

    def test_IfTimesGivenAreRational(self):
        #can't end before bedtime. bedtime can't be before start time.
        self.assertTrue(Babysit.check_times_for_rationality(self.babysitter, time(18,30), time(18,45), time(19,00)))
        self.assertTrue(Babysit.check_times_for_rationality(self.babysitter, time(18,00), time(19,30), time(19,45)))
        self.assertFalse(Babysit.check_times_for_rationality(self.babysitter, time(18,45), time(18,30), time(19,00)))
        self.assertFalse(Babysit.check_times_for_rationality(self.babysitter, time(18,00), time(19,45), time(19,30)))
        self.assertFalse(Babysit.check_times_for_rationality(self.babysitter, time(19,30), time(19,45), time(19,00)))

    def test_EverythingInSequence(self):
        #test if all methods run correctly when called by a single method        
        self.assertEqual(120, Babysit.test_and_calculate(self.babysitter, time(19,30), time(22,30), time(3,30)))
        self.assertEqual(None, Babysit.test_and_calculate(self.babysitter, time(13,30), time(22,30), time(3,30)))
        self.assertEqual(None, Babysit.test_and_calculate(self.babysitter, time(20,30), time(19,30), time(3,30)))

    def test_RawInputToTime(self):
        #test if function can convert raw input to time object.        
        self.assertEqual(time(12,34), self.babysitter.convert_raw_input('12:34'))
        self.assertEqual(None, self.babysitter.convert_raw_input('25:34'))
        self.assertEqual(None, self.babysitter.convert_raw_input('12:65'))
        self.assertEqual(None, self.babysitter.convert_raw_input('123654'))
        self.assertEqual(None, self.babysitter.convert_raw_input('3:45'))
        self.assertEqual(None, self.babysitter.convert_raw_input('agwgawea'))

    def test_InputStartTime(self):
        self.assertEqual(time(17,34), self.babysitter.handle_start_input('17:34'))        
        self.assertEqual(None, self.babysitter.handle_start_input('asdfdfs'))

    def test_InputBedTime(self):
        self.assertEqual(time(18,34), self.babysitter.handle_bed_input('18:34'))        
        self.assertEqual(None, self.babysitter.handle_bed_input('asdfdfs'))

    def test_InputEndTime(self):
        self.assertEqual(time(18,34), self.babysitter.handle_end_input('18:34'))        
        self.assertEqual(None, self.babysitter.handle_end_input('asdfdfs'))

if __name__ == '__main__':
    unittest.main()    
