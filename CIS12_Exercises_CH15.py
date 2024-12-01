
"""Exercise 15.10.2"""

class Date:
    """Represents a year, month, and day"""

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        date = f'{self.year:04d}-{self.month:02d}-{self.day:02d}'
        return date

    def is_after(date1, date2):
        if date1.year <= date2.year:
            if date1.month <= date2.month:
                if date1.day <= date2.day:
                    return False
        return True

date1 = Date(1933, 6, 22)
date2 = Date(1933, 9, 17)
print(date1.is_after(date2))