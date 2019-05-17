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

# 自定义的JsonResponse器,继承自HttpResponse,已不用
class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        # 重写content属性，返回rest_framework的JSON渲染器渲染的数据
        content = JSONRenderer().render(data)
        # 通过kwargs设置返回的数据类型为json
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


# 用户的注册和登录
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



# 根据频道名和新闻ID请求新闻详情
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
        return Response(status=status.HTTP_404_NOT_FOUND)
    # 获取电影详情资源
    if request.method == 'GET':
        news_serializer = NewsDetailSerializers(news, many=True)
        return Response(news_serializer.data)


# 设置单独的分类器,继承自PageNumberPagination
class MyPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 50
    #默认每页显示10个，可以通过传入/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    #最大页数不超过10
    max_page_size = 50
    #获取页码数的参数
    page_query_param = "page"


# 一下的14个类用于对14个频道列表进行分页的请求
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

