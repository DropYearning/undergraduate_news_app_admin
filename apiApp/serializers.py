
from rest_framework import serializers
from newsApp import models as m1
from userApp import models as m2


# 用户信息序列化器
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = m2.UserInfo
        fields = ('uuid', 'username', 'password')


# 新闻详情序列化器
class NewsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsEdu
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


# 新闻列表序列化器
class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsEdu
        fields = ('id', 'title', 'channelname', 'source', 'savetime', 'pubtime', 'link', 'havepic', 'picurl1', 'picurl2', 'picurl3', 'keywords')

