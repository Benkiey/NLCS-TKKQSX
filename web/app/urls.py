from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('thongke/', views.thongke, name='thongke'),
    path('quaythu/', views.quaythu, name='quaythu'),
]