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
    # 在左侧栏添加额外菜单
    def get_site_menu(self):  #名称不能改
        return [
            {
                # 这是自行添加的菜单项"统计"
                'title': '统计',
                'icon': 'fa fa-list-alt',
                'url': 'http://127.0.0.1:8000/xadmin/analysis',
            },
        ]
    # 设置后台顶部标题
    site_title = '新闻后台管理'
    # 设置后台底部标题
    site_footer = '毕业设计《基于Android的新闻推荐客户端设计与实现》 15051349 周亮'
    # 设置菜单可折叠
    menu_style = "accordion"


# 从你的app的view里引入你将要写的view，你也可以另外写一个py文件，把后台的view集中在一起方便管理
from .views import AnalysisView
# 注册自定义view (路由, 类名)
xadmin.site.register_view(r'analysis/$', AnalysisView, name='for_test')


# 基本设置参数
class BaseSetting(object):
    # 启用主题管理器   
    enable_themes = True
    # 使用主题 
    use_bootswatch = True


# 注册主题设置
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 注册全局参数
xadmin.site.register(views.CommAdminView, GlobalSetting)


# 模型配置类
class NewsCarAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-bars'  # 自定义图标,来源:fontawesome
    # list_display_links = ['link']  # 设置link字段为超链接
    show_terminal = True


class NewsDigitAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-desktop'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsDomesticAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-flag'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsEduAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-book'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsEstateAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-home'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsEntertainmentAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-film'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsFinanceAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-usd'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsGameAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-gamepad'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsInternationalAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-globe'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsInternetAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-cloud'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsMilitaryAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-fighter-jet'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsSocietyAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-users'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsSportAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-trophy'
    # list_display_links = ['link']  # 设置link字段为超链接


class NewsTechAdmin(object):
    list_display = ('title', 'source', 'savetime', 'pubtime', 'link', 'havepic')  # 自定义表在后台的显示列
    ordering = ('-savetime',)  # 排序（这里以日期排序，加‘-’表示降序）
    readonly_fields = ['id', 'channelname']  # 只读列
    exclude = ['html']  # 在编辑页面隐藏的字段
    model_icon = 'fa fa-flask'
    # list_display_links = ['link']  # 设置link字段为超链接


# 注册模型
xadmin.site.register(NewsCar, NewsCarAdmin)
xadmin.site.register(NewsDigit, NewsDigitAdmin)
xadmin.site.register(NewsDomestic, NewsDomesticAdmin)
xadmin.site.register(NewsEdu, NewsEduAdmin)
xadmin.site.register(NewsEstate, NewsEstateAdmin)
xadmin.site.register(NewsEntertainment, NewsEntertainmentAdmin)
xadmin.site.register(NewsFinance, NewsFinanceAdmin)
xadmin.site.register(NewsGame, NewsGameAdmin)
xadmin.site.register(NewsInternational, NewsInternationalAdmin)
xadmin.site.register(NewsInternet, NewsInternetAdmin)
xadmin.site.register(NewsMilitary, NewsMilitaryAdmin)
xadmin.site.register(NewsSociety, NewsSocietyAdmin)
xadmin.site.register(NewsSport, NewsSportAdmin)
xadmin.site.register(NewsTech, NewsTechAdmin)
