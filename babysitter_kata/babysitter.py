
from datetime import time as time

class Babysit(object):
    
    def __init__(self, starttime = time(00,00), bedtime = time(00,00), endtime = time(00,00)):
        self.start_time = starttime
        self.bed_time = bedtime
        self.end_time = endtime
        
    def check_start_time(self, starttime):
        #returns TRUE if start time is acceptable. Can start any time between 5:00 pm and 4:00 am
        if starttime >= time(17,00) or starttime <= time(04,00):
            return True
        else: return False

    def check_end_time(self, endtime):
        #returns TRUE if end time is acceptable. Must end at or before 4:00 am. May end as early as 5:00 pm
        if endtime <= time(04,00) or endtime >= time(17,00):
            return True
        else: return False

    def check_bed_time(self, bedtime):
        #returns TRUE if bedtime is acceptable. Must be between 5 pm and midnight
        if bedtime <= time(23,59) and bedtime >= time(17,00):
            return True
        elif bedtime == time(00,00):
            return True
        else: return False

if __name__ == '__main__':
    main = Babysit
    Babysit()
