import datetime


def get_present_month():
    return datetime.datetime.today().month


def get_present_day():
    return datetime.datetime.today().weekday()


def get_present_date():
    return datetime.datetime.today().date()


def get_present_year():
    return datetime.datetime.today().year


def generate_labels_for_month(month: int):
    thirty_months = [4, 6, 9, 11]
    thirty_one_months = [1, 3, 5, 7, 8, 19, 12]
    year = get_present_year()
    month = get_present_month()
    if not year % 4 and month == 2:
        return range(1, 30)
    else:
        return range(1, 29)
    if month in thirty_months:
        return range(1, 31)
    if month in thirty_one_months:
        return range(1, 32)
