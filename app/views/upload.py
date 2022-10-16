import os
import json
import random

from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect

from app.utils.MyMccabe import mccabe
from app.models import McCabe
from app.utils.form import UploadModelForm
from app.utils.unzip import unzip_file


def upload_list(request):
    if request.method == 'GET':
        up_form = UploadModelForm()
        return render(request, 'upload_list.html', {'form': up_form})
    up_form = UploadModelForm(data=request.POST, files=request.FILES)
    request.session.clear()
    if up_form.is_valid():
        up_form.instance.nid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        # 这个save之后可能会改成不save的
        up_form.save()  # TODO
        language = up_form.cleaned_data.get('language')
        file_object = up_form.cleaned_data.get('file')
        # 解压文件
        file_path = os.path.join(settings.MEDIA_ROOT, 'files', file_object.name)
        dst_dir = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, 'codes', os.path.splitext(file_object.name)[0])
        unzip_file(file_path, dst_dir)
        # 开始分析
        complex_res, complex_num, complex_sum = mccabe(dst_dir)
        complex_res_json = json.dumps(complex_res)
        McCabe.objects.create(path=dst_dir, complex_res=complex_res_json, complex_num=complex_num,
                              complex_sum=complex_sum)
        request.session['path'] = dst_dir
        context = {
            'path': dst_dir,
            'complex_res': complex_res,
            'complex_num': complex_num,
            'complex_sum': complex_sum
        }
        return render(request, 'calculate_mccabe.html', context)
    return render(request, 'upload_list.html', {'form': up_form})
