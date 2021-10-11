# -*- coding: utf-8 -*-

import datetime
from django.db import models

class Blog(models.Model):  
    name = models.CharField(verbose_name="博客名称", max_length=100)  
    tagline = models.TextField(verbose_name="博客标语")  

    def __str__(self):              
        return self.name  
      
class Author(models.Model):  
    name = models.CharField(verbose_name="作者姓名", max_length=50)  
    email = models.EmailField(verbose_name="邮箱", max_length=50)  

    def __str__(self):             
        return self.name  
       
class Entry(models.Model):  
    blog = models.ForeignKey(Blog, verbose_name="博客名称", on_delete=models.PROTECT, null=True,blank=True)  
    headline = models.CharField(verbose_name="大字标题", max_length=255)  
    body_text = models.TextField(verbose_name="博客内容",)  
    author = models.ManyToManyField(Author)  

    def __str__(self):              
        return self.headline
    
class School(models.Model):
    name = models.CharField(verbose_name='学校名字', max_length=32)
    address = models.CharField(verbose_name='学校地址', max_length=100)
    per = models.IntegerField(verbose_name='高考升学率', blank=True, null=True)
    date = models.DateTimeField(verbose_name='建校时间', default=datetime.datetime.now,  null=True, blank=True)
    
    class Meta:
        verbose_name = '学校名字'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name