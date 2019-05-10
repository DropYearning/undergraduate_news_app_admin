# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NewsCar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_car'


class NewsDigit(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_digit'


class NewsDomestic(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_domestic'


class NewsEdu(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_edu'


class NewsEntertainment(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_entertainment'


class NewsEstate(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_estate'


class NewsFinance(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_finance'


class NewsGame(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_game'


class NewsInternational(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_international'


class NewsInternet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_internet'


class NewsMilitary(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_military'


class NewsSociety(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_society'


class NewsSport(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_sport'


class NewsTech(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    savetime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    havepic = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    picurl1 = models.CharField(max_length=255, blank=True, null=True)
    picurl2 = models.CharField(max_length=255, blank=True, null=True)
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_tech'
