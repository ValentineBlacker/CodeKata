from datetime import time
import sys


class Babysit(object):

    """Calculate's a babysitter's pay. Pass 3 datetime objects to
    test_and_calculate() if using object from another program.
    Also runs handily in the terminal, and does error-checking
    on raw strings. """
    def __init__(self):
        self.start_to_bed = 12
        self.bed_to_mid = 8
        self.mid_to_end = 16

    def check_start_or_end_time(self, thetime):
        # returns TRUE if start time is acceptable. Can start any time between
        # 5:00 pm and 4:00 am
        if thetime >= time(17, 00) or thetime <= time(04, 00):
            return True
        else:
            return False

    def check_bed_time(self, bedtime):
        # returns TRUE if bedtime is acceptable.
        # Must be between 5 pm and midnight
        if bedtime <= time(23, 59) and bedtime >= time(17, 00):
            return True
        elif bedtime == time(00, 00):
            return True
        else:
            return False

    def check_times_for_rationality(self, starttime, bedtime, endtime):
        # make sure endtime is after bedtime, and bedtime is after starttime
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
        elif bedtime.hour == starttime.hour\
                and bedtime.minute >= starttime.minute:
            bedtime_ok = True

        if endtime_ok is True and bedtime_ok is True:
            return True
        else:
            return False

    def pay_start_to_bed(self, starttime, bedtime):
        """we deal only with hours here, since we get paid for a full hour at
        start even if we begin at the half hour, and if bedtime is in
        the middle of an hour we get paid the higher rate for that entire hour
        so we get paid at least 1 hour at the pre-bedtime rate"""
        bedtime_hour = int(bedtime.hour)
        if bedtime_hour == 0:
            bedtime_hour = 24
        if int(bedtime.minute) > 0:
            bedtime_hour += 1
        number_of_hours = (bedtime_hour - int(starttime.hour))
        if number_of_hours == 0:
            number_of_hours = 1
        total = (number_of_hours * self.start_to_bed)
        return total

    def pay_bed_to_mid(self, bedtime, endtime):
        # calculates to end time if end time is before midnight.
        # otherwise calculates to midnight. Partial hours paid
        # at higher pre-bedtime rate.
        ending_hour = int(endtime.hour)
        # if ending after midnight, calculate from midnight
        if ending_hour < 17:
            ending_hour = 24
        # otherwise round hour up
        elif int(endtime.minute) > 0:
            ending_hour += 1
        bedtime_hour = int(bedtime.hour)
        if int(bedtime.minute) > 0:
            bedtime_hour += 1
        number_of_hours = ending_hour - bedtime_hour
        total = (number_of_hours * self.bed_to_mid)
        return total

    def pay_mid_to_end(self, endtime):
        # calculates pay from midnight to end time
        # returns 0 if endtime is before midnight.
        # pays full hour for any partials.
        ending_hour = int(endtime.hour)
        if ending_hour > 4:
            return 0
        if int(endtime.minute) > 0:
            ending_hour += 1
        total = ending_hour * self.mid_to_end
        return total

    def calculate_total(self, starttime, bedtime, endtime):
        # calculates total pay
        stb = self.pay_start_to_bed(starttime, bedtime)
        btm = self.pay_bed_to_mid(bedtime, endtime)
        mte = self.pay_mid_to_end(endtime)
        total = stb+btm+mte
        return total

    def test_and_calculate(self, starttime, bedtime, endtime):
        # test input. returns NONE if times are not allowed,
        # otherwise returns total
        start_time_ok = self.check_start_or_end_time(starttime)
        end_time_ok = self.check_start_or_end_time(endtime)
        bed_time_ok = self.check_bed_time(bedtime)
        times_rational = self.check_times_for_rationality(
            starttime, bedtime, endtime)
        for x in [start_time_ok, end_time_ok, bed_time_ok, times_rational]:
            if x is False:
                return None
        else:
            total = self.calculate_total(starttime, bedtime, endtime)
        return total

    def convert_raw_input(self, rawstring):
        # converts raw input to date object.
        # returns NONE if input cannot be converted.
        if len(rawstring) > 5 or len(rawstring) < 4:
            return None
        if rawstring[:2].isdigit() and rawstring[3:].isdigit()\
                and rawstring[2] == ':':
            hours = int(rawstring[:2])
            minutes = int(rawstring[3:])
            if hours < 24 and minutes < 60:
                return time(hours, minutes)
            else:
                return None
        else:
            return None

    def handle_start_input(self, starttime):
        # checks start time input when called from terminal
        starttime = self.convert_raw_input(starttime)
        if starttime is None:
            print ('Please format time correctly. Program now exiting.\n')
            return None
        else:
            return starttime

    def handle_bed_input(self, bedtime):
        # checks bed time input when called from terminal
        bedtime = self.convert_raw_input(bedtime)
        if bedtime is None:
            print ('Please format time correctly. Program now exiting.\n')
            return None
        else:
            return bedtime

    def handle_end_input(self, endtime):
        # checks end time input when called from terminal
        endtime = self.convert_raw_input(endtime)
        if endtime is None:
            print ('Please format time correctly. Program now exiting.\n')
            return None
        else:
            return endtime

if __name__ == '__main__':
    main = Babysit
    babysitter = Babysit()
    print ('\nWelcome to the babysitter pay calculator! ' +
           'The babysitter gets paid ${0} \nfor each hour between'
           .format(babysitter.start_to_bed) +
           ' start time and bedtime, ${0} '.format(babysitter.bed_to_mid) +
           'for each hour between \nbetween bedtime and midnight' +
           ',and ${0} for each hour after'.format(babysitter.mid_to_end) +
           'midnight. The \n'
           'babysitter cannot begin before 17:00 and must leave before ' +
           '04:00. Partial \nhours are rounded up to full hours. \n\n' +
           'Times must be entered in 24-hour format.\n')

    raw_start = raw_input('Please enter a starting time in HH:MM format.\n\n')

    starttime = babysitter.handle_start_input(raw_start)
    print('\n')
    if starttime is None:
        sys.exit(0)
    raw_bed = raw_input('Please enter a bedtime in HH:MM format \n\n')

    bedtime = babysitter.handle_bed_input(raw_bed)
    print('\n')
    if bedtime is None:
        sys.exit(0)
    raw_end = raw_input('Please enter an ending time in HH:MM format \n\n')

    endtime = babysitter.handle_end_input(raw_end)
    print('\n')
    if endtime is None:
        sys.exit(0)
    total_pay = babysitter.test_and_calculate(starttime, bedtime, endtime)
    if total_pay is None:
        print('Problem with times. Start and end times must be between \n' +
              '17:00 and 04:00. Bedtime must be before midnight. Endtime \n' +
              'be after bedtime, and bedtime must be after start time. ' +
              'Program now exiting.\n')
    else:
        print ('The total pay will be ${0}\n'.format(total_pay))
    sys.exit(0)
