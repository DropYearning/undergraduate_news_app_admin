from django.contrib import admin
import xadmin
from xadmin import views

# 导入模型
from userApp.models import UserInfo


class UserInfoAdmin(object):
    list_display = ('uuid', 'username', 'password')  # 自定义表在后台的显示列
    model_icon = 'fa fa-user'  # 自定义图标,来源:fontawesome
    search_fields = ['username']  # 设置title为可搜索字段


# Register your models here.
xadmin.site.register(UserInfo, UserInfoAdmin)

