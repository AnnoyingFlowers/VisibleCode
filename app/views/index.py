import time

from django.shortcuts import render, redirect


def home(request):
    """
    首页
    """
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def link(request):
    return render(request, 'link.html')


def calculate(request):
    return render(request, 'upload_list.html')


def tables(request):
    return render(request, 'chart_list.html')

