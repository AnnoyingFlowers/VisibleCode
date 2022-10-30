import os
from datetime import datetime
import random

from django import forms
from django.forms import ModelForm

from app.models import Upload, McCabe


class UploadModelForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
        exclude = ['nid']
        error_messages = {
            'file': {
                'invalid_extension': '只能上传*.zip文件',
                'required': '请选择文件',
            }
        }

    def save(self, *args, **kwargs):
        # 这个地方写的和shit一样
        self.instance.file.name = os.path.splitext(self.instance.file.name)[0] + self.instance.nid + \
                                  os.path.splitext(self.instance.file.name)[1]
        return super().save(*args, **kwargs)
