from django.test import TestCase
import time

# Create your tests here.
from datetime import datetime
# timedelta 用于时间加减
from datetime import timedelta


print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))