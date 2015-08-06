
from datetime import time

class Babysit(object):
    
    def __init__(self, starttime = time(00,00), bedtime = time(00,00), endtime = time(00,00)):
        self.start_time = starttime
        self.bed_time = bedtime
        self.end_time = endtime
        
        self.start_to_bed = 12
        self.bed_to_mid = 8
        self.mid_to_end = 16
                
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

    def pay_start_to_bed(self, starttime, bedtime):
        #we deal only with hours here, since we get paid for a full hour at start
        #even if we begin at the half hour, and if bedtime is in the middle of an hour
        #we get paid the higher rate for that entire hour
        #so we get paid at least 1 hour at the pre-bedtime rate
        number_of_hours = abs(int(bedtime.hour) - int(starttime.hour))      
        if number_of_hours == 0:
            number_of_hours = 1
        return number_of_hours * self.start_to_bed
        

if __name__ == '__main__':
    main = Babysit
    Babysit()
