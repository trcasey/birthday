import datetime

def print_header():
    print('---------------------------------------')
    print('             BIRTHDAY APP              ')
    print('---------------------------------------')
    print()


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(date1, date2):
    pass


def print_birthday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)