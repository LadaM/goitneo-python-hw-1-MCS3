import calendar
from datetime import datetime, date, timedelta
from collections import defaultdict, OrderedDict

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
    week = timedelta(days=7) 
    tot_found = 0
    
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year).date()
        print(birthday_this_year)
        if birthday_this_year >= today and birthday_this_year < today + week:
            tot_found += 1
            print(datetime.strftime(birthday_this_year, "%A %d %B %y"))
            users_by_weekday[birthday_this_year.weekday()].append(user["name"])
    
    # sorting the result by the day of the week => Mo will always come first
    for d, n in sorted(users_by_weekday.items()):
        print(f"{calendar.day_name[d] if d < 5 else calendar.day_name[0]}: {', '.join(n)}")

# TODO: - what if birthday was last weekend?
#       - how to print the coming birthdays from today for each day of the week?
#           if today is Mo: Tuesday: ..., Wednesday: ... etc.
