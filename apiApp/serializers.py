
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


# 收藏列表序列化器
class SaveListSerializers(serializers.ModelSerializer):
    class Meta:
        model = m2.UserSavelist
        fields = ('username', 'news_id', 'news_title', 'news_keywords', 'news_channel', 'savetime')


# 访问历史列表序列化器
class HistoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = m2.UserHistorylist
        fields = ('username', 'news_id', 'news_title', 'news_keywords', 'news_channel', 'savetime')



