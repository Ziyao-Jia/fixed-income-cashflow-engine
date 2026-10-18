
import calendar

##按360天计算一年过了过了多少fraction of a year
def actual_360(start_date, end_date):
    t_fraction=t_fraction=(end_date-start_date).days/360
    return t_fraction

##按365天计算一年过了多少fraction of a year
def actual_365(start_date, end_date):
    t_fraction=(end_date-start_date).days/365
    return t_fraction

##按30天计算一个月，过了多少年
def thirty_360(start_date, end_date):
    d1 = min(start_date.day, 30)
    d2 = min(end_date.day, 30)
    year_diff  = end_date.year  - start_date.year
    month_diff = end_date.month - start_date.month
    day_diff   = d2 - d1
    days = 360 * year_diff + 30 * month_diff + day_diff
    return days / 360
    

def actual_actual(start_date, end_date):
    days = (end_date - start_date).days
    days_in_year = 366 if calendar.isleap(start_date.year) else 365
    return days / days_in_year

def get_year_fraction(start_date, end_date, convention):
    if convention=='ACT/360':
       return actual_360(start_date,end_date)
    elif convention=='ACT/365':
        return actual_365(start_date,end_date)
    elif convention=='30/360':
        return thirty_360(start_date,end_date)
    elif convention=="ACT/ACT":
        return actual_actual(start_date,end_date)
    else:

        raise ValueError(f"Unknown convention: {convention}")
