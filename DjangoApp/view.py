# -*- coding: utf-8 -*-

# @Author  : super
# @Time    : 2018/1/23
# @desc    :

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")
