from django.shortcuts import render
from django.http import HttpResponse
from newsApp import models as m1
from userApp import models as m2
from rest_framework import viewsets
from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.parsers import JSONParser
from .serializers import UserSerializers
from .serializers import NewsDetailSerializers
from .serializers import NewsListSerializers
import uuid
import time
import random

# 这个库非常强大 可以实现QuerySet的合并
from itertools import chain


# 自定义的JsonResponse器,继承自HttpResponse,已不用
class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        # 重写content属性，返回rest_framework的JSON渲染器渲染的数据
        content = JSONRenderer().render(data)
        # 通过kwargs设置返回的数据类型为json
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


# 用户的注册和登录API
@api_view(['GET', 'POST'])
def user_admin(request, username, password):
    if request.method == 'GET':
        user_byname = m2.UserInfo.objects.filter(username=username)
        user_bypwd = m2.UserInfo.objects.filter(username=username, password=password)
        if len(user_byname) == 0:
            return Response({'info': '登录失败:该用户尚未注册!', 'code': '501'})
        elif len(user_bypwd) == 0:
            return Response({'info': '登录失败:用户名和密码不正确!', 'code': '502'})
        elif len(user_bypwd) == 1:
            return Response({'info': '登陆成功!', 'code': '500'})
        elif len(user_byname) > 1:
            return Response({'info': '登录失败:未知错误,请查看后台数据', 'code': '503'})
    if request.method == 'POST':
        # 先判断用户名是否被占用
        user_byname = m2.UserInfo.objects.filter(username=username)
        if len(user_byname)>= 1:
            return Response({'info': '注册失败:该用户名已被使用!', 'code': '601'})
        else:
            # 生成一个唯一标志用户的主键UUID
            new_uuid = uuid.uuid4()
            m2.UserInfo.objects.create(uuid=new_uuid, username=username, password=password)
            return Response({'info': '注册成功!', 'code': '600'})


# 根据频道名和新闻ID请求新闻详情API
@api_view(['GET'])
def news_detail(request, channel, id):
    # python没有switch语句 只有用这么多if/else了
    if(channel =='edu'):
        news = m1.NewsEdu.objects.filter(id=id)
    elif(channel == 'domestic'):
        news = m1.NewsDomestic.objects.filter(id=id)
    elif (channel == 'finance'):
        news = m1.NewsFinance.objects.filter(id=id)
    elif (channel == 'internet'):
        news = m1.NewsInternet.objects.filter(id=id)
    elif (channel == 'estate'):
        news = m1.NewsEstate.objects.filter(id=id)
    elif (channel == 'car'):
        news = m1.NewsCar.objects.filter(id=id)
    elif (channel == 'sport'):
        news = m1.NewsSport.objects.filter(id=id)
    elif(channel == 'game'):
        news = m1.NewsGame.objects.filter(id=id)
    elif(channel == 'tech'):
        news = m1.NewsTech.objects.filter(id=id)
    elif (channel == 'entertainment'):
        news = m1.NewsEntertainment.objects.filter(id=id)
    elif (channel == 'military'):
        news = m1.NewsMilitary.objects.filter(id=id)
    elif (channel == 'digit'):
        news = m1.NewsDigit.objects.filter(id=id)
    elif (channel == 'society'):
        news = m1.NewsSociety.objects.filter(id=id)
    elif (channel == 'international'):
        news = m1.NewsInternational.objects.filter(id=id)
    if len(news) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND,)
    # 获取新闻详情资源
    if request.method == 'GET':
        news_serializer = NewsDetailSerializers(news, many=True)
        return Response(news_serializer.data)




# 随机从今天收录的新闻中推荐若干条API
@api_view(['GET'])
def news_recommend_random(request):
    # 设置推荐几条新闻
    para_news_count = 3
    year = time.strftime('%Y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    day = time.strftime('%d', time.localtime(time.time()))
    # 为了减少数据库检索压力,只从国内和国际两个范围最广的频道随机选出para_news_count篇文章推荐
    news_domestic = m1.NewsDomestic.objects.filter(savetime__year=year, savetime__month=month, savetime__day=day)
    news_international = m1.NewsInternational.objects.filter(savetime__year=year, savetime__month=month, savetime__day=day)

    # news_car = m1.NewsCar.objects.filter(savetime__year=year, savetime__month=month, savetime__day=day)
    # news_edu = m1.NewsEdu.objects.filter(savetime__year=year, savetime__month=month, savetime__day=day)

    int1 = random.randint(1, para_news_count-1)
    int2 = para_news_count - int1
    r1 = news_domestic.order_by('?')[:int1]
    r2 = news_international.order_by('?')[:int2]
    result = r1.union(r2)


    # 下面注释掉的是另一种Django ORM提供的原生方法,但是其不能用在结果的并集中
    # result = news_all.order_by('?')[:para_news_count]
    if request.method == 'GET':
        if(len(result) <= 0):
            return Response({'info': '找不到这样的新闻', 'code': '599'})
        result_serializer = NewsListSerializers(result, many=True)
        return Response(result_serializer.data)



# 根据频道名和新闻ID请求若干偏与之相似的推荐的新闻API
@api_view(['GET'])
def news_recommend_by_id(request, channel, id):
    # 设置推荐几条新闻
    para_news_count = 3
    # 判断是来自哪个频道的请求
    if(channel == 'edu'):
        news = m1.NewsEdu.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsEdu.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsEdu.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsEdu.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsEdu.objects.filter(keywords__contains=keyword1).filter(keywords__contains=keyword2).exclude(id=id)
        two_match2 =m1.NewsEdu.objects.filter(keywords__contains=keyword1).filter(keywords__contains=keyword3).exclude(id=id)
        two_match3 =m1.NewsEdu.objects.filter(keywords__contains=keyword3).filter(keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'domestic'):
        news = m1.NewsDomestic.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsDomestic.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsDomestic.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsDomestic.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsDomestic.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsDomestic.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsDomestic.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'international'):
        news = m1.NewsInternational.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsInternational.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsInternational.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsInternational.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsInternational.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsInternational.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsInternational.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'car'):
        news = m1.NewsCar.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsCar.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsCar.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsCar.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsCar.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsCar.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsCar.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'digit'):
        news = m1.NewsDigit.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsDigit.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsDigit.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsDigit.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsDigit.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsDigit.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsDigit.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'entertainment'):
        news = m1.NewsEntertainment.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsEntertainment.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsEntertainment.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsEntertainment.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsEntertainment.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsEntertainment.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsEntertainment.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'estate'):
        news = m1.NewsEstate.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsEstate.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsEstate.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsEstate.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsEstate.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsEstate.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsEstate.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'finance'):
        news = m1.NewsFinance.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsFinance.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsFinance.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsFinance.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsFinance.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsFinance.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsFinance.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'game'):
        news = m1.NewsGame.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsGame.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsGame.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsGame.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsGame.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsGame.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsGame.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'internet'):
        news = m1.NewsInternet.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsInternet.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsInternet.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsInternet.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsInternet.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsInternet.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsInternet.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'military'):
        news = m1.NewsMilitary.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsMilitary.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsMilitary.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsMilitary.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsMilitary.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsMilitary.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsMilitary.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)

    elif (channel == 'society'):
        news = m1.NewsSociety.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsSociety.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsSociety.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsSociety.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsSociety.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsSociety.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsSociety.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'sport'):
        news = m1.NewsSport.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsSport.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsSport.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsSport.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsSport.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsSport.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsSport.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)
    elif (channel == 'tech'):
        news = m1.NewsTech.objects.get(id=id)
        keywords_list = news.keywords.split('/')
        keyword1 = keywords_list[0]
        keyword2 = keywords_list[1]
        keyword3 = keywords_list[2]
        k1_result = m1.NewsTech.objects.filter(keywords__contains=keyword1).exclude(id=id)
        k2_result = m1.NewsTech.objects.filter(keywords__contains=keyword2).exclude(id=id)
        k3_result = m1.NewsTech.objects.filter(keywords__contains=keyword3).exclude(id=id)
        two_match1 = m1.NewsTech.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword2).exclude(id=id)
        two_match2 = m1.NewsTech.objects.filter(keywords__contains=keyword1).filter(
            keywords__contains=keyword3).exclude(id=id)
        two_match3 = m1.NewsTech.objects.filter(keywords__contains=keyword3).filter(
            keywords__contains=keyword2).exclude(id=id)


    # 筛选出匹配一个关键词的QS
    one_match_qs = k1_result | k2_result | k3_result
    # 筛选出匹配两个关键词的QS
    two_match_qs = two_match1 | two_match2 | two_match3
    # 如果two_match_qs个数>=para_news_count
    if(len(two_match_qs) >= para_news_count):
        # 将two_match_qs按发布时间排序,取最新的para_news_count个作为结果
        result = two_match_qs.order_by('-pubtime')[:para_news_count]
    else:
        # 若two_match_qs数量不足, 先将其加入到结果中
        result = one_match_qs | two_match_qs

    if request.method == 'GET':
        if(len(result) > para_news_count):
            r = result.order_by('-pubtime')[:para_news_count]
            result_serializer = NewsListSerializers(r, many=True)
            return Response(result_serializer.data)
        elif(len(result) == 0):
            return Response({'info': '找不到这样的新闻', 'code': 599})
        else:
            result_serializer = NewsListSerializers(result, many=True)
            return Response(result_serializer.data)
        # return Response({'info': '找不到这样的新闻', 'code': len(result)})






# 设置单独的分类器,继承自PageNumberPagination
class MyPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 10
    #默认每页显示10个，可以通过传入/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    #最大页数不超过10
    max_page_size = 50
    #获取页码数的参数
    page_query_param = "page"


# 一下的14个类用于对14个频道列表进行分页的请求API
class EduNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsEdu.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class DomesticNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsDomestic.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class InternationalNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsInternational.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class CarNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsCar.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class DigitNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsDigit.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class EntertainmentNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsEntertainment.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class EstateNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsEstate.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class FinanceNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsFinance.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class GameNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsGame.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class InternetNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsInternet.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class MilitaryNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsMilitary.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class SocietyNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsSociety.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class SportNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsSport.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination


class TechNewsListSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m1.NewsTech.objects.all().order_by('-savetime')
    # 指定序列化的类
    serializer_class = NewsListSerializers
    # 使用自定义的分页器
    pagination_class = MyPagination

