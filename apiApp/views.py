from django.shortcuts import render
from django.http import HttpResponse
from newsApp import models as m1
from userApp import models as m2
from rest_framework import viewsets
from .serializers import UserSerializers


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = m2.UserInfo.objects.all()
    # 指定序列化的类
    serializer_class = UserSerializers