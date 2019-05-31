from django.test import TestCase

# Create your tests here.
import  time

day = time.strftime('%d', time.localtime(time.time()))

print(type(day))