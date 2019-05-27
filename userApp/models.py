from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uuid = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name='用户名')
    password = models.CharField(max_length=255, blank=True, null=True, verbose_name='密码')

    class Meta:
        managed = False
        db_table = 'user_info'
        verbose_name_plural = '用户信息'


class UserSavelist(models.Model):
    tablepk = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    news_id = models.CharField(max_length=255, blank=True, null=True)
    news_title = models.CharField(max_length=255, blank=True, null=True)
    news_keywords = models.CharField(max_length=255, blank=True, null=True)
    news_channel = models.CharField(max_length=255, blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_savelist'
        verbose_name_plural = '用户收藏'


class UserHistorylist(models.Model):
    tablepk = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    news_id = models.CharField(max_length=255, blank=True, null=True)
    news_title = models.CharField(max_length=255, blank=True, null=True)
    news_keywords = models.CharField(max_length=255, blank=True, null=True)
    news_channel = models.CharField(max_length=255, blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_historylist'
        verbose_name_plural = '访问历史'

