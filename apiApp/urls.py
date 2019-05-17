from django.conf.urls import include, url
from rest_framework import routers
from apiApp import views

# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'edu', views.EduNewsListSet)
route.register(r'domestic', views.DomesticNewsListSet)
route.register(r'international', views.InternationalNewsListSet)
route.register(r'car', views.CarNewsListSet)
route.register(r'digit', views.DigitNewsListSet)
route.register(r'entertainment', views.EntertainmentNewsListSet)
route.register(r'estate', views.EstateNewsListSet)
route.register(r'finance', views.FinanceNewsListSet)
route.register(r'game', views.GameNewsListSet)
route.register(r'internet', views.InternetNewsListSet)
route.register(r'military', views.MilitaryNewsListSet)
route.register(r'society', views.SocietyNewsListSet)
route.register(r'sport', views.SportNewsListSet)
route.register(r'tech', views.TechNewsListSet)



# 注册上一级的路由地址并添加
urlpatterns = [
    url('newlist/', include(route.urls)),
]