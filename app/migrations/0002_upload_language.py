# Generated by Django 3.2.9 on 2022-10-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='language',
            field=models.IntegerField(choices=[(1, 'C'), (2, 'C++'), (3, 'Python'), (4, 'Java'), (5, 'JavaScript'), (6, 'C#'), (7, '其他')], default=1, verbose_name='语言'),
        ),
    ]