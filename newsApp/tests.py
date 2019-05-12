from django.test import TestCase

# Create your tests here.
from datetime import datetime
# timedelta 用于时间加减
from datetime import timedelta


from newsApp import newsUpdate_DB

newsUpdate_DB.Update.update(newsUpdate_DB.Update)
