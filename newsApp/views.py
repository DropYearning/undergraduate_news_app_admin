from django.shortcuts import render
from django.db.models import Count
from newsApp import models
from newsApp.py import mytime
from newsApp.py import newsUpdate_DB
from django.db.models.aggregates import Count,Sum

import time
import json



# Create your views here.
from xadmin.views import CommAdminView


# API信息页视图
class ApiInfoView(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "API信息"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        # 下面你可以接着写你自己的东西了，写完记得添加到context里面就可以了
        return render(request, 'apiInfo.html', context)  # 最后指定自定义的template模板，并返回context


# 统计视图类(旧的实现)
class AnalysisView(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "统计"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面

        # 获取各频道已收录新闻数量
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

        # 获取各频道今日更新的数量
        allUpdateCount = 0
        carUpdateCount = 0
        digitUpdateCount = 0
        domesticUpdateCount = 0
        eduUpdateCount = 0
        entertainmentUpdateCount = 0
        estateUpdateCount = 0
        financeUpdateCount = 0
        gameUpdateCount = 0
        internationalUpdateCount = 0
        internetUpdateCount = 0
        militaryUpdateCount = 0
        societyUpdateCount = 0
        sportUpdateCount = 0
        techUpdateCount = 0

        year = time.strftime('%Y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = time.strftime('%d', time.localtime(time.time()))
        allLogItems = models.NewsLog.objects.filter(updatetime__year=year,
                                                 updatetime__month=month, updatetime__day=day)
        for logItem in allLogItems:
            allUpdateCount = allUpdateCount + logItem.all_count
            carUpdateCount = carUpdateCount + logItem.car_count
            digitUpdateCount = digitUpdateCount + logItem.digit_count
            domesticUpdateCount = domesticUpdateCount + logItem.demostic_count
            eduUpdateCount = eduUpdateCount + logItem.edu_count
            entertainmentUpdateCount = entertainmentUpdateCount + logItem.entertainment_count
            estateUpdateCount = estateUpdateCount + logItem.estate_count
            financeUpdateCount = financeUpdateCount + logItem.finance_count
            gameUpdateCount = gameUpdateCount + logItem.game_count
            internationalUpdateCount = internationalUpdateCount + logItem.international_count
            internetUpdateCount = internetUpdateCount + logItem.internet_count
            militaryUpdateCount = militaryUpdateCount + logItem.military_count
            societyUpdateCount = societyUpdateCount + logItem.society_count
            sportUpdateCount = sportUpdateCount + logItem.sport_count
            techUpdateCount = techUpdateCount + logItem.tech_count

        # 获取最后一次更新时间
        lastUpdateTime = models.NewsLog.objects.latest('updatetime').updatetime

        # # 获取下一次更新时间(下一小时)
        # nextUpdateTime = mytime.get_next_hour()
        nextUpdateTime = mytime.next_5_minute()

        # 注入context
        context['lastUpdateTime'] = lastUpdateTime
        context['nextUpdateTime'] = nextUpdateTime
        context["carNewsCount"] = carNewsCount
        context["digitNewsCount"] = digitNewsCount
        context["domesticNewsCount"] = domesticNewsCount
        context["eduNewsCount"] = eduNewsCount
        context["entertainmentNewsCount"] = entertaionmentNewsCount
        context["estateNewsCount"] = estateNewsCount
        context["financeNewsCount"] = finaceNewsCount
        context["gameNewsCount"] = gameNewsCount
        context["internationalNewsCount"] = internationalNewsCount
        context["internetNewsCount"] = internetNewsCount
        context["militaryNewsCount"] = militaryNewsCount
        context["societyNewsCount"] = societyNewsCount
        context["sportNewsCount"] = sportNewsCount
        context["techNewsCount"] = techNewsCount
        context["allNewsCount"] = allNewsCount
        context["allUpdateCount"] = allUpdateCount
        context["carUpdateCount"] = carUpdateCount
        context["digitUpdateCount"] = digitUpdateCount
        context["domesticUpdateCount"] = domesticUpdateCount
        context["eduUpdateCount"] = eduUpdateCount
        context["entertainmentUpdateCount"] = entertainmentUpdateCount
        context["estateUpdateCount"] = estateUpdateCount
        context["financeUpdateCount"] = financeUpdateCount
        context["gameUpdateCount"] = gameUpdateCount
        context["internationalUpdateCount"] = internationalUpdateCount
        context["internetUpdateCount"] = internetUpdateCount
        context["militaryUpdateCount"] = militaryUpdateCount
        context["societyUpdateCount"] = societyUpdateCount
        context["sportUpdateCount"] = sportUpdateCount
        context["techUpdateCount"] = techUpdateCount
        # 注入
        return render(request, 'analysis.html', context)


# 重写分析页View, 优化查询策略
class AnalysisView_rebuild(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "统计"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面

        # 获取各频道已收录新闻数量
        carNewsCount = models.NewsCar.objects.all().count()
        digitNewsCount = models.NewsDigit.objects.all().count()
        domesticNewsCount = models.NewsDomestic.objects.all().count()
        eduNewsCount = models.NewsEdu.objects.all().count()
        entertainmentNewsCount = models.NewsEntertainment.objects.all().count()
        estateNewsCount = models.NewsEstate.objects.all().count()
        finaceNewsCount = models.NewsFinance.objects.all().count()
        gameNewsCount = models.NewsGame.objects.all().count()
        internationalNewsCount = models.NewsInternational.objects.all().count()
        internetNewsCount = models.NewsInternet.objects.all().count()
        militaryNewsCount = models.NewsMilitary.objects.all().count()
        societyNewsCount = models.NewsSociety.objects.all().count()
        sportNewsCount = models.NewsSport.objects.all().count()
        techNewsCount = models.NewsTech.objects.all().count()
        # allNewsCount是已收录的新闻数量总和
        allNewsCount = carNewsCount + digitNewsCount + domesticNewsCount + eduNewsCount + entertainmentNewsCount + estateNewsCount + finaceNewsCount + gameNewsCount + internationalNewsCount + internetNewsCount + militaryNewsCount + societyNewsCount + sportNewsCount + techNewsCount

        # # 获取今日更新的数目
        year = time.strftime('%Y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = time.strftime('%d', time.localtime(time.time()))
        allLogItems = models.NewsLog.objects.filter(updatetime__year=year,
                                                 updatetime__month=month, updatetime__day=day)
        carToday = allLogItems.aggregate(carTodayCount=Sum('car_count'))
        digitToday = allLogItems.aggregate(digitTodayCount=Sum('digit_count'))
        domesticToday = allLogItems.aggregate(domesticTodayCount=Sum('demostic_count'))
        entertainmentToday = allLogItems.aggregate(entertainmentTodayCount=Sum('entertainment_count'))
        eduToday = allLogItems.aggregate(eduTodayCount=Sum('edu_count'))
        estateToday = allLogItems.aggregate(estateTodayCount=Sum('estate_count'))
        financeToday = allLogItems.aggregate(financeTodayCount=Sum('finance_count'))
        gameToday = allLogItems.aggregate(gameTodayCount=Sum('game_count'))
        internationalToday = allLogItems.aggregate(internationalTodayCount=Sum('international_count'))
        internetToday = allLogItems.aggregate(internetTodayCount=Sum('internet_count'))
        militaryToday = allLogItems.aggregate(militaryTodayCount=Sum('military_count'))
        societyToday = allLogItems.aggregate(societyTodayCount=Sum('society_count'))
        sportToday = allLogItems.aggregate(sportTodayCount=Sum('sport_count'))
        techToday = allLogItems.aggregate(techTodayCount=Sum('tech_count'))
        # 提取Sum的结果
        carUpdateCount = carToday['carTodayCount']
        digitUpdateCount = digitToday['digitTodayCount']
        domesticUpdateCount = domesticToday['domesticTodayCount']
        eduUpdateCount = eduToday['eduTodayCount']
        entertainmentUpdateCount = entertainmentToday['entertainmentTodayCount']
        estateUpdateCount = estateToday['estateTodayCount']
        financeUpdateCount = financeToday['financeTodayCount']
        gameUpdateCount = gameToday['gameTodayCount']
        internationalUpdateCount = internationalToday['internationalTodayCount']
        internetUpdateCount = internetToday['internetTodayCount']
        militaryUpdateCount = militaryToday['militaryTodayCount']
        societyUpdateCount = societyToday['societyTodayCount']
        sportUpdateCount = sportToday['sportTodayCount']
        techUpdateCount = techToday['techTodayCount']
        allUpdateCount = carUpdateCount + digitUpdateCount + domesticUpdateCount + eduUpdateCount + entertainmentUpdateCount + estateUpdateCount + financeUpdateCount + gameUpdateCount + internationalUpdateCount + internetUpdateCount + militaryUpdateCount + societyUpdateCount + sportUpdateCount + techUpdateCount

        # 获取最后一次更新时间
        lastUpdateTime = models.NewsLog.objects.latest('updatetime').updatetime

        # # 获取下一次更新时间(下一小时)
        # nextUpdateTime = mytime.get_next_hour()
        nextUpdateTime = mytime.next_5_minute()

        # 注入context到analysis.html中
        context['lastUpdateTime'] = lastUpdateTime
        context['nextUpdateTime'] = nextUpdateTime
        context["carNewsCount"] = carNewsCount
        context["digitNewsCount"] = digitNewsCount
        context["domesticNewsCount"] = domesticNewsCount
        context["eduNewsCount"] = eduNewsCount
        context["entertainmentNewsCount"] = entertainmentNewsCount
        context["estateNewsCount"] = estateNewsCount
        context["financeNewsCount"] = finaceNewsCount
        context["gameNewsCount"] = gameNewsCount
        context["internationalNewsCount"] = internationalNewsCount
        context["internetNewsCount"] = internetNewsCount
        context["militaryNewsCount"] = militaryNewsCount
        context["societyNewsCount"] = societyNewsCount
        context["sportNewsCount"] = sportNewsCount
        context["techNewsCount"] = techNewsCount
        context["allNewsCount"] = allNewsCount
        context["carUpdateCount"] = carUpdateCount
        context["digitUpdateCount"] = digitUpdateCount
        context["domesticUpdateCount"] = domesticUpdateCount
        context["eduUpdateCount"] = eduUpdateCount
        context["entertainmentUpdateCount"] = entertainmentUpdateCount
        context["estateUpdateCount"] = estateUpdateCount
        context["financeUpdateCount"] = financeUpdateCount
        context["gameUpdateCount"] = gameUpdateCount
        context["internationalUpdateCount"] = internationalUpdateCount
        context["internetUpdateCount"] = internetUpdateCount
        context["militaryUpdateCount"] = militaryUpdateCount
        context["societyUpdateCount"] = societyUpdateCount
        context["sportUpdateCount"] = sportUpdateCount
        context["techUpdateCount"] = techUpdateCount
        context["allUpdateCount"] = allUpdateCount
        return render(request, 'statistic.html', context)


# 更新用view
class UpdateView(CommAdminView):
    def get(self, request):
        # 必须super一下继承CommAdminView里面的context，不然侧栏没有对应数据
        context = super().get_context()
        title = "统计"  # 定义顶栏子标题
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})  # 把面包屑变量添加到context里面
        context["title"] = title  # 把面包屑变量添加到context里面
        # 调用newsUpdate_DB.py执行数据库更新
        newsUpdate_DB.Update.update(newsUpdate_DB.Update)

        # 获取各频道已收录新闻数量
        carNewsCount = models.NewsCar.objects.all().count()
        digitNewsCount = models.NewsDigit.objects.all().count()
        domesticNewsCount = models.NewsDomestic.objects.all().count()
        eduNewsCount = models.NewsEdu.objects.all().count()
        entertainmentNewsCount = models.NewsEntertainment.objects.all().count()
        estateNewsCount = models.NewsEstate.objects.all().count()
        finaceNewsCount = models.NewsFinance.objects.all().count()
        gameNewsCount = models.NewsGame.objects.all().count()
        internationalNewsCount = models.NewsInternational.objects.all().count()
        internetNewsCount = models.NewsInternet.objects.all().count()
        militaryNewsCount = models.NewsMilitary.objects.all().count()
        societyNewsCount = models.NewsSociety.objects.all().count()
        sportNewsCount = models.NewsSport.objects.all().count()
        techNewsCount = models.NewsTech.objects.all().count()
        # allNewsCount是已收录的新闻数量总和
        allNewsCount = carNewsCount + digitNewsCount + domesticNewsCount + eduNewsCount + entertainmentNewsCount + estateNewsCount + finaceNewsCount + gameNewsCount + internationalNewsCount + internetNewsCount + militaryNewsCount + societyNewsCount + sportNewsCount + techNewsCount

        # 获取今日更新的数目
        year = time.strftime('%Y', time.localtime(time.time()))
        month = time.strftime('%m', time.localtime(time.time()))
        day = time.strftime('%d', time.localtime(time.time()))
        allLogItems = models.NewsLog.objects.filter(updatetime__year=year,
                                                    updatetime__month=month, updatetime__day=day)
        carToday = allLogItems.aggregate(carTodayCount=Sum('car_count'))
        digitToday = allLogItems.aggregate(digitTodayCount=Sum('digit_count'))
        domesticToday = allLogItems.aggregate(domesticTodayCount=Sum('demostic_count'))
        entertainmentToday = allLogItems.aggregate(entertainmentTodayCount=Sum('entertainment_count'))
        eduToday = allLogItems.aggregate(eduTodayCount=Sum('edu_count'))
        estateToday = allLogItems.aggregate(estateTodayCount=Sum('estate_count'))
        financeToday = allLogItems.aggregate(financeTodayCount=Sum('finance_count'))
        gameToday = allLogItems.aggregate(gameTodayCount=Sum('game_count'))
        internationalToday = allLogItems.aggregate(internationalTodayCount=Sum('international_count'))
        internetToday = allLogItems.aggregate(internetTodayCount=Sum('internet_count'))
        militaryToday = allLogItems.aggregate(militaryTodayCount=Sum('military_count'))
        societyToday = allLogItems.aggregate(societyTodayCount=Sum('society_count'))
        sportToday = allLogItems.aggregate(sportTodayCount=Sum('sport_count'))
        techToday = allLogItems.aggregate(techTodayCount=Sum('tech_count'))
        # 提取Sum的结果
        carUpdateCount = carToday['carTodayCount']
        digitUpdateCount = digitToday['digitTodayCount']
        domesticUpdateCount = domesticToday['domesticTodayCount']
        eduUpdateCount = eduToday['eduTodayCount']
        entertainmentUpdateCount = entertainmentToday['entertainmentTodayCount']
        estateUpdateCount = estateToday['estateTodayCount']
        financeUpdateCount = financeToday['financeTodayCount']
        gameUpdateCount = gameToday['gameTodayCount']
        internationalUpdateCount = internationalToday['internationalTodayCount']
        internetUpdateCount = internetToday['internetTodayCount']
        militaryUpdateCount = militaryToday['militaryTodayCount']
        societyUpdateCount = societyToday['societyTodayCount']
        sportUpdateCount = sportToday['sportTodayCount']
        techUpdateCount = techToday['techTodayCount']
        allUpdateCount = carUpdateCount + digitUpdateCount + domesticUpdateCount + eduUpdateCount + entertainmentUpdateCount + estateUpdateCount + financeUpdateCount + gameUpdateCount + internationalUpdateCount + internetUpdateCount + militaryUpdateCount + societyUpdateCount + sportUpdateCount + techUpdateCount

        # 获取本次更新时间
        lastUpdateTime = models.NewsLog.objects.latest('updatetime').updatetime
        # 获取本次更新数量
        lastUpdateCount = models.NewsLog.objects.latest('updatetime').all_count
        # # 获取下一次更新时间(下一小时)
        # nextUpdateTime = mytime.get_next_hour()
        nextUpdateTime = mytime.next_5_minute()

        # 注入context
        context['lastUpdateTime'] = lastUpdateTime
        context['lastUpdateCount'] = lastUpdateCount
        context['nextUpdateTime'] = nextUpdateTime
        context["carNewsCount"] = carNewsCount
        context["digitNewsCount"] = digitNewsCount
        context["domesticNewsCount"] = domesticNewsCount
        context["eduNewsCount"] = eduNewsCount
        context["entertainmentNewsCount"] = entertainmentUpdateCount
        context["estateNewsCount"] = estateNewsCount
        context["financeNewsCount"] = finaceNewsCount
        context["gameNewsCount"] = gameNewsCount
        context["internationalNewsCount"] = internationalNewsCount
        context["internetNewsCount"] = internetNewsCount
        context["militaryNewsCount"] = militaryNewsCount
        context["societyNewsCount"] = societyNewsCount
        context["sportNewsCount"] = sportNewsCount
        context["techNewsCount"] = techNewsCount
        context["allNewsCount"] = allNewsCount
        context["carUpdateCount"] = carUpdateCount
        context["digitUpdateCount"] = digitUpdateCount
        context["domesticUpdateCount"] = domesticUpdateCount
        context["eduUpdateCount"] = eduUpdateCount
        context["entertainmentUpdateCount"] = entertainmentUpdateCount
        context["estateUpdateCount"] = estateUpdateCount
        context["financeUpdateCount"] = financeUpdateCount
        context["gameUpdateCount"] = gameUpdateCount
        context["internationalUpdateCount"] = internationalUpdateCount
        context["internetUpdateCount"] = internetUpdateCount
        context["militaryUpdateCount"] = militaryUpdateCount
        context["societyUpdateCount"] = societyUpdateCount
        context["sportUpdateCount"] = sportUpdateCount
        context["techUpdateCount"] = techUpdateCount
        context["allUpdateCount"] = allUpdateCount
        return render(request, 'fetch.html', context)






