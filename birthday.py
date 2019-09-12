import datetime
from banner import banner

banner("BIRTHDAY", "Samuel")



def main():
    birthday = get_birthday_from_user()
    now = datetime.date.today()
    num_days = calculate_days_between_dates(birthday, now)
    print_birthday_info(num_days)

def get_birthday_from_user():
    print("What is your birthday?")
    year = int(input("Year (YYYY)? "))
    month = int(input("Month (MM)? "))
    day = int(input("Day (DD)?"))

    birthday = datetime.date(year, month, day)
    return birthday

def calculate_days_between_dates(date1, date2):
    this_year = datetime.date(date2.year, date1.month, date1.day)
    dt = this_year - date2
    return dt.days


def print_birthday_info(number_of_days):
    print(number_of_days)







def print_birthday_info(number_of_days):
    print(number_of_days)


main()