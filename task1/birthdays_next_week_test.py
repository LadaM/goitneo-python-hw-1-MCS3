from get_birthdays_next_week import get_birthdays_next_week
from datetime import datetime, timedelta
from faker import Faker 

# test that one result is found
test_1 = [
    {"name": "Precious One", "birthday": datetime.today() + timedelta(days=30)},
    {"name": "Justin Ferrow", "birthday": datetime.today() + timedelta(days=15)},
    {"name": "Marry Poppins", "birthday": datetime.today() + timedelta(days=6)},
]

# 10 birthdays in next 10 days, expect 7 selected to test that today + 7 days isn't included
test_2 = [ {"name": f"Name-{i}",  "birthday" : datetime.now() + timedelta(days=i)} for i in range(10)]
get_birthdays_next_week(test_2)

# generating 100 random users
mock = Faker()
users = list()
for _ in range(100):
    bd = mock.date()
    name = mock.name()
    users.append({"name": name, "birthday": datetime.strptime(bd, "%Y-%m-%d")})

get_birthdays_next_week(users)