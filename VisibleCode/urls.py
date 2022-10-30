"""VisibleCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app.views import index, upload, chart, calculate

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 主页
    path('home/', index.home),
    path('', index.home),
    path('index/', index.index),
    path('index/team/', index.team),
    path('index/link/', index.link),

    # 计算界面
    path('calculate/calculate_mccabe/', calculate.calculate_mccabe),

    # 分析界面
    path('upload/upload_list/', upload.upload_list),
    path('chart/upload_tree/', chart.upload_tree),
    path('chart/upload_treemap/', chart.upload_treemap),

    # 图表界面
    path('chart/chart_list/', chart.chart_list),
    path('chart/chart_line/', chart.chart_line),
    path('chart/chart_pie/', chart.chart_pie),
    path('chart/chart_bar/', chart.chart_bar),
    path('chart/chart_scatter/', chart.chart_scatter),

]

