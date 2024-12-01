
"""Exercise 14.12.2"""

class Time:
    """Represents a time of day."""

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def print_time(time):
    time = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(time)

def time_is_after(t1, t2):
    #"""Checks whether `t1` is after `t2`.
    #    Tests were altered to make sense.
    #    >>> time_is_after((3, 2, 1), (3, 2, 0))
    #    True
    #    >>> time_is_after((3, 2, 1), (3, 2, 1))
    #    False
    #    >>> time_is_after((11, 12, 0), (9, 40, 0))
    #    True
    #    """
    t1, t2 = make_time(*t1), make_time(*t2)
    if t1.hour <= t2.hour:
        if t1.minute <= t2.minute:
            if t1.second <= t2.second:
                return False
    return True

"""Exercise 14.12.3"""

class Date:
    """Represents a year, month, and day"""

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    date = f'{date.year:04d}-{date.month:02d}-{date.day:02d}'
    print(date)

#date = make_date(1933, 6, 22)
#print_date(date)

def date_is_after(d1, d2):
    """Checks whether `d1` is after `d2`.
    >>> date_is_after((1933, 6, 22), (1933, 6, 20))
    True
    >>> date_is_after((1933, 6, 22), (1933, 6, 22))
    False
    >>> date_is_after((2005, 5, 31), (1961, 10, 26))
    True
    """
    d1, d2 = make_date(*d1), make_date(*d2)
    if d1.year <= d2.year:
        if d1.month <= d2.month:
            if d1.day <= d2.day:
                return False
    return True
