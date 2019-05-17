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

import xadmin

admin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('user/<str:username>/<str:password>', user_admin),
    path('detail/<str:channel>/<str:id>/', news_detail),
    path('recommendbyid/<str:channel>/<str:id>/', news_recommend_by_id),
    path('', include('apiApp.urls')),    #添加的路由地址
]
