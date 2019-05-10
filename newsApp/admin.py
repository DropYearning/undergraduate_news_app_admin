from django.contrib import admin
import xadmin
from xadmin import views
# 导入models
from newsApp.models import NewsCar
from newsApp.models import NewsDigit
from newsApp.models import NewsDomestic
from newsApp.models import NewsEdu
from newsApp.models import NewsEntertainment
from newsApp.models import NewsEstate
from newsApp.models import NewsFinance
from newsApp.models import NewsGame
from newsApp.models import NewsInternational
from newsApp.models import NewsInternet
from newsApp.models import NewsMilitary
from newsApp.models import NewsSociety
from newsApp.models import NewsSport
from newsApp.models import NewsTech


# 全局设置参数
class GlobalSetting(object):
    # 设置后台顶部标题
    site_title ='新闻后台管理'
    # 设置后台底部标题
    site_footer ='<基于Android的新闻推荐客户端设计与实现> 15051349 周亮'
    # 设置菜单可折叠
    menu_style = "accordion"

class BaseSetting(object):
    # 启用主题管理器   
    enable_themes =True
    # 使用主题 
    use_bootswatch =True



# 注册主题设置
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 注册全局参数
xadmin.site.register(views.CommAdminView, GlobalSetting)

# 模型配置类
class NewsCarAdmin(object):
    list_display = ('title', 'savetime', 'link') # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname'] #只读列
    exclude = ['html'] #在编辑页面隐藏的字段




# 注册模型
xadmin.site.register(NewsCar, NewsCarAdmin)
xadmin.site.register(NewsDigit)
xadmin.site.register(NewsDomestic)
xadmin.site.register(NewsEdu)
xadmin.site.register(NewsEstate)
xadmin.site.register(NewsFinance)
xadmin.site.register(NewsGame)
xadmin.site.register(NewsInternational)
xadmin.site.register(NewsInternet)
xadmin.site.register(NewsMilitary)
xadmin.site.register(NewsSociety)
xadmin.site.register(NewsSport)
xadmin.site.register(NewsTech)


