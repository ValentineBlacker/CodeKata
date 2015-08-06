
import datetime

class Babysit(object):
    
    def __init__(self):
        pass
        
    def check_start_time(self, starttime, endtime):
        if starttime >= datetime.time(17,00) or starttime < datetime.time(04,00):
            return True
        else: return False



if __name__ == '__main__':
    main = Babysit
    Babysit()
