import os
import json
import random

from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect

from app.models import McCabe
from app.utils.MyMccabe import mccabe
from app.utils.unzip import unzip_file
from app.utils.form import UploadModelForm


def upload_list(request):
    if request.method == 'GET':
        up_form = UploadModelForm()
        return render(request, 'upload_list.html', {'form': up_form, 'display': 'display: none'})
    up_form = UploadModelForm(data=request.POST, files=request.FILES)
    request.session.clear()
    if up_form.is_valid():
        up_form.instance.nid = str(datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999)))
        # 这个save之后可能会改成不save的
        up_form.save()  # TODO
        language = up_form.cleaned_data.get('language')
        file_object = up_form.cleaned_data.get('file')
        # 解压文件
        file_name = os.path.splitext(file_object.name)[0] + up_form.instance.nid + os.path.splitext(file_object.name)[1]
        file_path = os.path.join(settings.MEDIA_ROOT, 'files', file_name)
        dst_dir = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, 'codes', os.path.splitext(file_name)[0])
        unzip_file(file_path, dst_dir)
        # 开始分析
        # 以后删掉，集合到专门算mccabe的地方  TODO
        complex_res, complex_num, complex_sum = mccabe(dst_dir)
        complex_res_json = json.dumps(complex_res)
        McCabe.objects.create(path=dst_dir, complex_res=complex_res_json, complex_num=complex_num,
                              complex_sum=complex_sum)
        request.session['path'] = dst_dir
        context = {
            'form': up_form,
            'path': dst_dir,
            'complex_res': complex_res,
            'complex_num': complex_num,
            'complex_sum': complex_sum,
            'display': ''
        }
        return render(request, 'upload_list.html', context)
    return render(request, 'upload_list.html', {'form': up_form, 'display': 'display: none'})
