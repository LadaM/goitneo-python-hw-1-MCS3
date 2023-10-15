import calendar
from datetime import datetime, timedelta
from collections import defaultdict

# Data format users = {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}
# Output format birthdays_next_week = {'Monday': ['Bill Gates'], 'Thursday': ['Jan Koum']} 
#   sorted by weekday Mo -> Fr, Sa & Su are moved to the coming Monday
# Algo:
#   for each user in the list
#       - if their BD is during next 7 days -> store the weekday & user name
#       - map WD number to WD name, special case - Sa & Su map to Mo
#   return the dict weekday_name : [users]
def get_birthdays_next_week(users):
    users_by_weekday = defaultdict(list)
    today = datetime.now().date()
    curr_weekday = today.weekday()

    def is_monday(day_number: int):
        return day_number == 0
    
    def is_weekend(day_number: int):
        return day_number == 5 or day_number == 6
    
    if is_weekend(curr_weekday):
        print((f"Today is {calendar.day_name[curr_weekday]} and we don't do evaluations"
              "on weekends. Enjoy your free time!"))
        return
    
    weekend = timedelta(days=2 if is_monday(curr_weekday) else 0)
    week = timedelta(days=7) 
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year).date()
        # including past weekend and exluding next weekend if day is Monday
        if (birthday_this_year >= today - weekend and 
            birthday_this_year < today + week - weekend):
            users_by_weekday[birthday_this_year.weekday()].append(user["name"])
    
    # move the weekend birthdays to Monday
    for weekday in sorted(users_by_weekday.keys()):
        if is_weekend(weekday):
            users_by_weekday[0].extend(users_by_weekday.pop(weekday))

    # sorting the result by the day of the week => Mo will always come first
    for d, n in sorted(users_by_weekday.items()):
        print(f"{calendar.day_name[d]}: {', '.join(n)}")