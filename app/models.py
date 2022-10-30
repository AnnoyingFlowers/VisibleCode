from django.core import validators
from django.db import models


# 建库语句：create database Visible_Code DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
# 别搞错了，要不然中文报错！

# Create your models here.

class Upload(models.Model):
    language_choices = (
        (1, 'C'),
        (2, 'C++'),
        (3, 'Python'),
        (4, 'Java'),
        (5, 'JavaScript'),
        (6, 'C#'),
        (7, '其他'),
    )
    nid = models.CharField(verbose_name='nid', default=0, max_length=64)
    language = models.IntegerField(verbose_name='语言', choices=language_choices, default=1)
    file = models.FileField(verbose_name='文件', max_length=128, upload_to='files',
                            validators=[validators.FileExtensionValidator(['zip'])])


class McCabe(models.Model):
    path = models.FilePathField(verbose_name='路径', null=True)
    complex_res = models.JSONField(verbose_name='细节', null=True)
    complex_num = models.IntegerField(verbose_name='复杂度>threshold的方法个数')
    complex_sum = models.IntegerField(verbose_name='复杂度之和')
