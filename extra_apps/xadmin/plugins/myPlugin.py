from xadmin.views import BaseAdminPlugin
 # 继承BaseAdminPlugin方法


# 添加自定义功能列
class TerminalPlugin(BaseAdminPlugin):
    show_terminal = False

        # 初始化是否加载插件
    def init_request(self, *args, **kwargs):
        return bool(self.show_terminal)

    # 实现html代码，这里的href可以返回一个url
    def terminal_link(self, instance):
        return '<a class="btn btn-default btn-sm"  href="www.baidu.com"> <i class="fa fa-terminal"></i> Terminal</a>'

    # 设置以下标签才能实现正常显示列
    terminal_link.short_description = ' '
    terminal_link.allow_tags = True
    terminal_link.allow_export = False
    terminal_link.is_column = False

    # 显示字段加入新增的字段
    def get_list_display(self, list_display):
        if self.show_terminal:
            list_display.append('terminal_link')
            self.admin_view.terminal_link = self.terminal_link
        return list_display