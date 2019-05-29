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
from apiApp.views import get_news_detail
from apiApp.views import user_admin
from apiApp.views import get_recommend_by_id
from apiApp.views import get_recommend_random
from apiApp.views import save_admin
from apiApp.views import history_admin
from apiApp.views import get_user_savelist
from apiApp.views import get_user_historylist
from apiApp.views import check_savelist
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
    # 查询用户是否收藏过某条新闻
    path('checksave/<str:username>/<str:news_id>', check_savelist),
    # 添加收藏/取消收藏API
    path('save/<str:username>/<str:news_channelname>/<str:news_id>', save_admin),
    # 添加访问记录/删除 API
    path('history/<str:username>/<str:news_channelname>/<str:news_id>', history_admin),
    # 新闻详情API
    path('detail/<str:channel>/<str:id>/', get_news_detail),
    # 获取用户收藏列表
    path('savelist/<str:username>', get_user_savelist),
    # 获取用户访问历史列表
    path('historylist/<str:username>', get_user_historylist),
    # 按新闻ID推荐API
    path('rcm4news/<str:channel>/<str:id>/', get_recommend_by_id),
    # 随机推荐3篇新闻API
    path('rcm4random3/', get_recommend_random),
    # 随机推荐10篇新闻(作为初始推荐列表)API
    path('rcm4random10/', get_recommend_random),
]
