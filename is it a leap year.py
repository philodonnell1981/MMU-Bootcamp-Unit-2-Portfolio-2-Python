month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    #Return true for leap years, false for non leap years
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    #return number of days in that month in that year
    if not 1 <= month <= 12:
        return 'Invalid month'
    # year 2017
    #month 2
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))