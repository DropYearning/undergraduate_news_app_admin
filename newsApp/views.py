from django.shortcuts import render
from django.db.models import Count
from newsApp import models
import time
import json

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


# 统计视图类
class AnalysisView(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "统计"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面

        # dict用于向HTML页面传递参数
        dict = { }
        # 统计新闻条数
        carNewsCount = models.NewsCar.objects.all().aggregate(Count('id'))['id__count']
        digitNewsCount = models.NewsDigit.objects.all().aggregate(Count('id'))['id__count']
        domesticNewsCount = models.NewsDomestic.objects.all().aggregate(Count('id'))['id__count']
        eduNewsCount = models.NewsEdu.objects.all().aggregate(Count('id'))['id__count']
        entertaionmentNewsCount = models.NewsEntertainment.objects.all().aggregate(Count('id'))['id__count']
        estateNewsCount = models.NewsEstate.objects.all().aggregate(Count('id'))['id__count']
        finaceNewsCount = models.NewsFinance.objects.all().aggregate(Count('id'))['id__count']
        gameNewsCount = models.NewsGame.objects.all().aggregate(Count('id'))['id__count']
        internationalNewsCount = models.NewsInternational.objects.all().aggregate(Count('id'))['id__count']
        internetNewsCount = models.NewsInternet.objects.all().aggregate(Count('id'))['id__count']
        militaryNewsCount = models.NewsMilitary.objects.all().aggregate(Count('id'))['id__count']
        societyNewsCount = models.NewsSociety.objects.all().aggregate(Count('id'))['id__count']
        sportNewsCount = models.NewsSport.objects.all().aggregate(Count('id'))['id__count']
        techNewsCount = models.NewsTech.objects.all().aggregate(Count('id'))['id__count']
        allNewsCount = carNewsCount + digitNewsCount + domesticNewsCount + eduNewsCount + entertaionmentNewsCount + estateNewsCount + finaceNewsCount + gameNewsCount + internationalNewsCount + internetNewsCount + militaryNewsCount + societyNewsCount + sportNewsCount + techNewsCount
        # 数据库中各频道新闻数量
        dict["carNewsCount"] = carNewsCount
        dict["digitNewsCount"] = digitNewsCount
        dict["domesticNewsCount"] = domesticNewsCount
        dict["eduNewsCount"] = eduNewsCount
        dict["entertaionmentNewsCount"] = entertaionmentNewsCount
        dict["estateNewsCount"] = estateNewsCount
        dict["finaceNewsCount"] = finaceNewsCount
        dict["gameNewsCount"] = gameNewsCount
        dict["internationalNewsCount"] = internationalNewsCount
        dict["internetNewsCount"] = internetNewsCount
        dict["militaryNewsCount"] = militaryNewsCount
        dict["societyNewsCount"] = societyNewsCount
        dict["sportNewsCount"] = sportNewsCount
        dict["techNewsCount"] = techNewsCount
        dict["allNewsCount"] = allNewsCount

        todayUpdateCount = 0
        year = time.strftime('%Y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = time.strftime('%d', time.localtime(time.time()))
        logItems = models.NewsLog.objects.filter(updatetime__year=year,
                                                 updatetime__month=month, updatetime__day=day)
        for logItem in logItems:
            todayUpdateCount = todayUpdateCount + logItem.all_count

        # 今日入库总数量
        dict["todayUpdateCount"] = todayUpdateCount


        #  最后指定自定义的template模板，并注入context
        return render(request, 'analysis.html',  {'dict': json.dumps(dict)})
        # 发送数据给JavaScript

