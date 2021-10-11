# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [  
    path('', views.index, name='index'),
    path('account/<int:page>/', views.pageInfo),      
    path('account/<str:campus>/', views.buildingInfo),    
]
