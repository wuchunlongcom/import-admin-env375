# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [       
    url(r'index1/$', views.index1, name='index1'),
    
    url(r'', views.index, name='index'),   #必须放在最后
]
