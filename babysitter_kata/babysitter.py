
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

    def check_times_for_rationality(self, starttime, bedtime, endtime):
        #make sure endtime is after bedtime, and bedtime is after starttime
        endtime_ok = False
        if endtime.hour < 5:
            endtime_ok = True
        elif endtime.hour > bedtime.hour:
            endtime_ok = True
        elif endtime.hour == bedtime.hour and endtime.minute >= bedtime.minute:
            endtime_ok = True
        bedtime_ok = False
        
        if bedtime.hour > starttime.hour:
            bedtime_ok = True
        elif bedtime.hour == starttime.hour and bedtime.minute >= starttime.minute:
            bedtime_ok = True
            
        if endtime_ok == True and bedtime_ok == True:
            return True
        else: return False
            

    def pay_start_to_bed(self, starttime, bedtime):
        #we deal only with hours here, since we get paid for a full hour at start
        #even if we begin at the half hour, and if bedtime is in the middle of an hour
        #we get paid the higher rate for that entire hour
        #so we get paid at least 1 hour at the pre-bedtime rate
        bedtime_hour = int(bedtime.hour)
        if bedtime_hour == 0:
            bedtime_hour = 24
        if int(bedtime.minute) > 0:
            bedtime_hour+= 1
        #print bedtime_hour
        number_of_hours = (bedtime_hour - int(starttime.hour))      
        if number_of_hours == 0:
            number_of_hours = 1
        return (number_of_hours * self.start_to_bed)

    def pay_bed_to_mid(self, bedtime, endtime):
        #calculates to end time if end time is before midnight.
        #otherwise calculates to midnight. Partial hours paid
        #at higher pre-bedtime rate.
        ending_hour = int(endtime.hour)
        #if ending after midnight, calculate from midnight
        if ending_hour < 17:
            ending_hour = 24
        #otherwise round hour up
        elif int(endtime.minute) > 0:
            ending_hour += 1
        bedtime_hour = int(bedtime.hour)
        if int(bedtime.minute) > 0:
            bedtime_hour += 1        
        number_of_hours = ending_hour - bedtime_hour        
        return (number_of_hours * self.bed_to_mid)       
        

    def pay_mid_to_end(self, endtime):
        #calculates pay from midnight to end time
        #returns 0 if endtime is before midnight.
        #pays full hour for any partials.
        ending_hour = int(endtime.hour)
        if ending_hour > 4:
            return 0
        if int(endtime.minute) > 0:
            ending_hour += 1
        return ending_hour * self.mid_to_end

    def calculate_total(self, starttime, bedtime, endtime):
        stb = self.pay_start_to_bed(starttime, bedtime)        
        btm = self.pay_bed_to_mid(bedtime, endtime)        
        mte = self.pay_mid_to_end(endtime)        
        total = stb+btm+mte
        return total

if __name__ == '__main__':
    main = Babysit
    Babysit()
