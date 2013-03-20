#!/usr/bin/python

month_days = [('jan',31), ('feb',28), ('mar',31), ('apr',30), ('may',31), ('jun',30), 
              ('jul',31), ('aug',31), ('sep',30), ('oct',31), ('nov',30), ('dec',31)]

# assume 1 is sunday, 2 is monday ..... and 7 is saturday

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False

# 1 January 1900 was a Monday

# Firstly, calculate what day is 1 January 1901

for month, day in month_days:
    pass    
