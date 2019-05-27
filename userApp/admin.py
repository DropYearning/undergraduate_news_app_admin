from django.contrib import admin
import xadmin
from xadmin import views

# 导入模型
from userApp.models import UserInfo
from userApp.models import UserHistorylist
from userApp.models import UserSavelist


class UserInfoAdmin(object):
    list_display = ('uuid', 'username', 'password')  # 自定义表在后台的显示列
    model_icon = 'fa fa-user'  # 自定义图标,来源:fontawesome
    search_fields = ['username']  # 设置title为可搜索字段


class UserHistoryAdmin(object):
    list_display = ('username', 'news_title', 'news_channel', 'news_keywords', 'savetime')  # 自定义表在后台的显示列
    model_icon = 'fa fa-history'  # 自定义图标,来源:fontawesome
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    list_filter = ['username']  # 设置过滤器作用字段


class UserSavedAdmin(object):
    list_display = ('username', 'news_title', 'news_channel', 'news_keywords', 'savetime')  # 自定义表在后台的显示列
    model_icon = 'fa fa-heart'  # 自定义图标,来源:fontawesome
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    list_filter = ['username']  # 设置过滤器作用字段


# Register your models here.
xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(UserHistorylist, UserHistoryAdmin)
xadmin.site.register(UserSavelist, UserSavedAdmin)

