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

app_name = 'lib'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('addBook/', views.addBook, name='addBook'),
    path('delBook/<int:book_id>', views.delBook, name='delBook'),

               ]
