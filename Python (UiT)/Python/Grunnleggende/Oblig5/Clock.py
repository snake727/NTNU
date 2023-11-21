class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, minute=0, second=0):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.hour = int(hour)
        self.minute = int(minute)
        self.sec = int(second)

    def inc_second(self):
        if self.sec == 59:
            self.sec = 0
            if self.minute == 59:
                self.minute = 0
                if self.hour == 23:
                    self.hour = 0
                    if self.month == 2:
                        if ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
                            if self.day == 29:
                                self.day = 1
                                self.month += 1
                            else:
                                self.day += 1
                        else: 
                            if self.day == 28:
                                self.day = 1
                                self.month += 1
                            else:
                                self.day += 1
                    elif self.month % 2 == 0:
                        if self.day == 30:
                            self.day = 1
                            self.month += 1
                        else:
                            self.day += 1
                    else:
                        if self.day == 31:
                            self.day = 1
                            self.month += 1
                        else: 
                            self.day += 1
        else:
            self.sec += 1

    def inc_minute(self):
        if self.minute == 59:
            self.minute = 0
            self.sec = 0
            if self.hour == 23:
                self.hour = 0
                if self.month == 2:
                    if ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
                        if self.day == 29:
                            self.day = 1
                            self.month += 1
                        else:
                            self.day += 1
                    else: 
                        if self.day == 28:
                            self.day = 1
                            self.month += 1
                        else:
                            self.day += 1
                elif self.month % 2 == 0:
                    if self.day == 30:
                        self.day = 1
                        self.month += 1
                    else:
                        self.day += 1
                else:
                    if self.day == 31:
                        self.day = 1
                        self.month += 1
                    else: 
                        self.day += 1
            self.minute = 0
        else:
            self.minute += 1
        
    def inc_hour(self):
        if self.hour == 23:
            self.hour = 0
            self.minute = 0
            self.sec = 0
            if self.month == 2:
                if ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
                    if self.day == 29:
                        self.day = 1
                        self.month += 1
                    else:
                            self.day += 1
                else: 
                    if self.day == 28:
                        self.day = 1
                        self.month += 1
                    else:
                        self.day += 1
            elif self.month % 2 == 0:
                if self.day == 30:
                    self.day = 1
                    self.month += 1
                else:
                    self.day += 1
            else:
                if self.day == 31:
                    self.day = 1
                    self.month += 1
                else: 
                    self.day += 1
        else:
            self.hour += 1

    def inc_day(self):
        if self.month == 2:
            if ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
                if self.day == 29:
                    self.day = 1
                    self.month += 1
                else:
                        self.day += 1
            else: 
                if self.day == 28:
                    self.day = 1
                    self.month += 1
                else:
                    self.day += 1
        elif self.month % 2 == 0:
            if self.day == 30:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        else:
            if self.day == 31:
                self.day = 1
                self.month += 1
            else: 
                self.day += 1

    def inc_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

    def inc_year(self):
        self.year += 1
        
    def clock_as_string(self):
        clockstring = str(f"{self.day:02d}:{self.month:02d}:{self.year:04d}:{self.hour:02d}:{self.minute:02d}:{self.sec:02d}")
        return clockstring
    
    def set_clock(self, day, month, year, hour, minute, sec):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.min = minute
        self.sec = sec