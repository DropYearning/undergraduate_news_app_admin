"""news_app_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apiApp.views import news_detail
from apiApp.views import user_admin
from apiApp.views import news_recommend_by_id
from apiApp.views import news_recommend_random

import xadmin

admin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),

    # Xadmin后台管理页面
    path('xadmin/', xadmin.site.urls),
    # 新闻列表API(RESTful_framework)
    path('', include('apiApp.urls')),    # 从apiApp.urls中导入的路由
    # 注册登录API
    path('user/<str:username>/<str:password>', user_admin),
    # 新闻详情API
    path('detail/<str:channel>/<str:id>/', news_detail),
    # 按新闻ID推荐API
    path('rcm4news/<str:channel>/<str:id>/', news_recommend_by_id),
    # 随机推荐API
    path('rcm4random/', news_recommend_random),


]
