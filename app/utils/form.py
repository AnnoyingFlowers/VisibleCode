from django import forms
from django.forms import ModelForm

from app.models import Upload, McCabe


class UploadModelForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
        error_messages = {
            'file': {
                'invalid_extension': '只能上传*.zip文件',
                'required': '请选择文件',
            }
        }
