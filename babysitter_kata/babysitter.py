
from datetime import time

class Babysit(object):
    
    def __init__(self):
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
        total = (number_of_hours * self.start_to_bed)
        return total

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
        total = (number_of_hours * self.bed_to_mid)
        return total
        

    def pay_mid_to_end(self, endtime):
        #calculates pay from midnight to end time
        #returns 0 if endtime is before midnight.
        #pays full hour for any partials.
        ending_hour = int(endtime.hour)
        if ending_hour > 4:
            return 0
        if int(endtime.minute) > 0:
            ending_hour += 1
        total = ending_hour * self.mid_to_end
        return total

    def calculate_total(self, starttime, bedtime, endtime):
        #calculates total pay
        stb = self.pay_start_to_bed(starttime, bedtime)        
        btm = self.pay_bed_to_mid(bedtime, endtime)        
        mte = self.pay_mid_to_end(endtime)        
        total = stb+btm+mte
        return total

    def test_and_calculate(self, starttime, bedtime, endtime):
        #test input. returns NONE if times are not allowed, otherwise returns total
        start_time_ok = self.check_start_time(starttime)
        end_time_ok =self.check_end_time(endtime)
        bed_time_ok = self.check_bed_time(bedtime)
        times_rational = self.check_times_for_rationality(starttime, bedtime, endtime)
        for x in [start_time_ok, end_time_ok, bed_time_ok, times_rational]:
            if x == False:
                return None
        else: total = self.calculate_total(starttime, bedtime, endtime)
        return total

    def convert_raw_input(self, rawstring):
        #converts raw input to date object.
        #returns NONE if input cannot be converted.
        if len(rawstring) >5 or len(rawstring) < 4:
            return None
        if rawstring[:2].isdigit() and rawstring[3:].isdigit() and rawstring[2] == ':':       
            hours = int(rawstring[:2])
            minutes = int(rawstring[3:])
            if hours < 24 and minutes < 60:
                return time(hours,minutes)
            else: return None
        else: return None

    def handle_start_input(self, starttime):
        starttime = self.convert_raw_input(starttime)
        if starttime == None:
            print ('please format time correctly')
            return None
        if self.check_start_time(starttime) == False:
            print ('start time cannot be earlier than 17:00 or later than 04:00')
            return None
        else: return starttime

    def handle_bed_input(self, bedtime):
        bedtime = self.convert_raw_input(bedtime)
        if bedtime == None:
            print ('please format time correctly')
            return None
        if self.check_bed_time(bedtime) == False:
            print ('bed time must be between 17:00 and 0:00')
            return None
        else: return bedtime

    
        
    
                
if __name__ == '__main__':
    main = Babysit
    Babysit()
