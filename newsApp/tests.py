from django.test import TestCase

# Create your tests here.
from datetime import datetime
# timedelta 用于时间加减
from datetime import timedelta


def get_next_hour():
    now = datetime.now()
    minute = (now.strftime('%a,%b,%d %H:%M'))
    next_hour = now + timedelta(hours=1)

    print(next_hour)
