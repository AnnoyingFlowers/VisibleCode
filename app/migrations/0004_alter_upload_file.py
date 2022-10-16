# Generated by Django 3.2.9 on 2022-10-15 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(max_length=128, upload_to='files', validators=[django.core.validators.FileExtensionValidator(['zip', 'png'])], verbose_name='文件'),
        ),
    ]