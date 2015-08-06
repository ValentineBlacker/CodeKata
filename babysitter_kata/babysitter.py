
import datetime

class Babysit(object):
    
    def __init__(self, starttime = datetime.time(00,00), bedtime = datetime.time(00,00), endtime = datetime.time(00,00)):
        self.start_time = starttime
        self.bed_time = bedtime
        self.end_time = endtime
        
    def check_start_time(self, starttime):
        #returns TRUE if start time is acceptable. Can start any time between 5:00 pm and 4:00 am
        if starttime >= datetime.time(17,00) or starttime <= datetime.time(04,00):
            return True
        else: return False

    def check_end_time(self, endtime):
        #returns TRUE if end time is acceptable. Must end at or before 4:00 am. May end as early as 5:00 pm
        if endtime <= datetime.time(04,00) or endtime >= datetime.time(17,00):
            return True
        else: return False


if __name__ == '__main__':
    main = Babysit
    Babysit()
