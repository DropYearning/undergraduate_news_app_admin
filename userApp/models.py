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

