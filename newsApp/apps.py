from django.apps import AppConfig


class TestappConfig(AppConfig):
    name = 'newsApp'
    verbose_name = '新闻'
    # App的默认图标为其中第一个model的icon
