from django.shortcuts import render

# Create your views here.
from xadmin.views import CommAdminView


class TestView(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "测试子菜单1"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        return render(request, 'test.html', context)  # 最后指定自定义的template模板，并返回context


class AnalysisView(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "统计"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        return render(request, 'analysis.html', context)  # 最后指定自定义的template模板，并返回context
