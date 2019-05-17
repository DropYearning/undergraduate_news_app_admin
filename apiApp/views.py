from django.shortcuts import render
from django.http import HttpResponse
from newsApp import models as m1
from userApp import models as m2
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import UserSerializers
from .serializers import EduNewsSerializers


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m2.UserInfo.objects.all()
    # 指定序列化的类
    serializer_class = UserSerializers

class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        # 重写content属性，返回rest_framework的JSON渲染器渲染的数据
        content = JSONRenderer().render(data)
        # 通过kwargs设置返回的数据类型为json
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


def news_edu_list(request):
    if request.method == 'GET':
        # 查询所有电影信息
        news = m1.NewsEdu.objects.filter(id='f2eb7534c5f01815bf0558b0bcebaa9c')
        # 实例化一个序列化器，指示为多条数据的序列化
        news_serializer = EduNewsSerializers(news, many=True)
        # 返回序列化的json数据
        return JsonResponse(news_serializer.data)


