from django.contrib import admin
from django.urls import path
from . import views

#định nghĩa một đường dẫn
urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('thongke/', views.thongke, name='thongke'),

    path('thongke50/', views.thongke50, name='thongke50'),
    path('thongke100/', views.thongke100, name='thongke100'),
    path('thongke200/', views.thongke200, name='thongke200'),
    path('thongke500/', views.thongke500, name='thongke500'),
    
    path('quaythu/', views.quaythu, name='quaythu'),

]