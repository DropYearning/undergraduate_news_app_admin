# Generated by Django 2.2.1 on 2019-05-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCar',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('channelname', models.CharField(blank=True, db_column='channelName', max_length=8, null=True)),
                ('source', models.CharField(blank=True, max_length=16, null=True)),
                ('pubtime', models.DateTimeField(blank=True, null=True)),
                ('savetime', models.DateTimeField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('havepic', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('html', models.TextField(blank=True, null=True)),
                ('picurl1', models.CharField(blank=True, max_length=255, null=True)),
                ('picurl2', models.CharField(blank=True, max_length=255, null=True)),
                ('picurl3', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'news_car',
                'managed': False,
            },
        ),
    ]
