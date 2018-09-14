# coding: utf-8
"""
@project = pythontest
@file = urls
@author = liu_bo
@create_time = 2018/9/14 10:22
@describe = 
"""
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'), ]
