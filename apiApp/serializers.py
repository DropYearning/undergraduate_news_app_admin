
from rest_framework import serializers
from newsApp import models as m1
from userApp import models as m2


# 用户信息序列化器
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = m2.UserInfo
        fields = ('uuid', 'username', 'password')


# 各频道新闻序列化器
class EduNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsEdu
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class DomesticNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsDomestic
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class FianceNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsFinance
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class InternetNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsInternet
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class EstateNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsEstate
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class CarNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsCar
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class SportNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsSport
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class GameNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsGame
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class TechNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsTech
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class EntertainmentNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsEntertainment
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class MilitaryNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsMilitary
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class DigitNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsDigit
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class SocietyNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsSociety
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')


class InternationalNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = m1.NewsInternational
        fields = ('id', 'title', 'channelname', 'source', 'pubtime', 'link', 'havepic', 'html', 'picurl1', 'picurl2', 'picurl3', 'keywords')

