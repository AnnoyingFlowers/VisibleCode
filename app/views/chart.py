from django.http import JsonResponse
from django.shortcuts import render

from app.models import McCabe


def chart_list(request):
    """
    数据统计页面
    """
    return render(request, 'chart_list.html')


def chart_scatter(request):
    """
    构建散点图
    """
    result = {

    }
    return JsonResponse(result)


def chart_bar(request):
    """
    构建柱状图
    """
    path = request.session.get('path')
    row_object = McCabe.objects.filter(path=path).first()
    print(row_object.complex_res)
    complex_res_dict = eval(row_object.complex_res)
    title_text = 'mccabe'
    x_axis = []
    series_data = []
    for _path, _info in complex_res_dict.items():
        for _filename, _fileinfo in _info.items():
            for key, value in _fileinfo.items():
                x_axis.append(_filename + ': ' + key)
                series_data.append(value)
    result = {
        'status': True,
        'data': {
            'title_text': title_text,
            'x_axis': x_axis,
            'series_data': series_data,
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """
    构建饼状图
    """

    pie_data = [
        {'value': 1048, 'name': 'Search Engine'},
        {'value': 735, 'name': 'Direct'},
        {'value': 580, 'name': 'Email'},
        {'value': 484, 'name': 'Union Ads'},
        {'value': 300, 'name': 'Video Ads'}
    ]
    result = {
        'status': True,
        'data': pie_data
    }
    return JsonResponse(result)


def chart_line(request):
    """
    构建折线图
    """
    path = request.session.get('path')
    row_object = McCabe.objects.filter(path=path).first()
    print(row_object.complex_res)
    complex_res_dict = eval(row_object.complex_res)
    title_text = 'mccabe'
    x_axis = []
    series_data = []
    for _path, _info in complex_res_dict.items():
        for _filename, _fileinfo in _info.items():
            for key, value in _fileinfo.items():
                x_axis.append(_filename + ': ' + key)
                series_data.append(value)
    result = {
        'status': True,
        'data': {
            'title_text': title_text,
            'x_axis': x_axis,
            'series_data': series_data,
        }
    }
    return JsonResponse(result)
