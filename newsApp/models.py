# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 国内新闻
class NewsDomestic(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_domestic'
        # 如果设置verbose_name会出现名字多一个s的情况
        verbose_name_plural = '国内'



# 国际新闻
class NewsInternational(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_international'
        verbose_name_plural = '国际'


# 汽车新闻
class NewsCar(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_car'
        verbose_name_plural = '汽车'


# 数码新闻
class NewsDigit(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_digit'
        verbose_name_plural = '数码'


# 教育新闻
class NewsEdu(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_edu'
        verbose_name_plural = '教育'


# 娱乐新闻
class NewsEntertainment(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_entertainment'
        verbose_name_plural = '娱乐'


# 房地产新闻
class NewsEstate(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_estate'
        verbose_name_plural = '房地产'


# 财经新闻
class NewsFinance(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_finance'
        verbose_name_plural = '财经'


# 游戏新闻
class NewsGame(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_game'
        verbose_name_plural = '游戏'


# 互联网新闻
class NewsInternet(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_internet'
        verbose_name_plural = '互联网'


# 军事新闻
class NewsMilitary(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_military'
        verbose_name_plural = '军事'


# 社会新闻
class NewsSociety(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_society'
        verbose_name_plural = '社会'


# 体育新闻
class NewsSport(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")
    picurl3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_sport'
        verbose_name_plural = '体育'


# 科技新闻
class NewsTech(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name="主键")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="标题")
    channelname = models.CharField(db_column='channelName', max_length=255, blank=True, null=True, verbose_name="频道")  # Field name made lowercase.
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="来源")
    pubtime = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    savetime = models.DateTimeField(blank=True, null=True, verbose_name="收录时间")
    link = models.CharField(max_length=255, blank=True, null=True, verbose_name="原链接")
    havepic = models.IntegerField(blank=True, null=True, verbose_name="图片数")
    content = models.TextField(blank=True, null=True, verbose_name="正文")
    html = models.TextField(blank=True, null=True, verbose_name="HTML")
    picurl1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL1")
    picurl2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL2")
    picurl3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片URL3")

    class Meta:
        managed = False
        db_table = 'news_tech'
        verbose_name_plural = '科技'
