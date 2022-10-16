# Generated by Django 3.2.9 on 2022-10-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_upload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='McCabe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_res', models.JSONField(null=True, verbose_name='细节')),
                ('complex_num', models.IntegerField(verbose_name='复杂度>threshold的方法个数')),
                ('complex_sum', models.IntegerField(verbose_name='复杂度之和')),
            ],
        ),
    ]
