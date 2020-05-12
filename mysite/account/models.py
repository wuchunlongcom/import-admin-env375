# -*- coding: utf-8 -*-

import datetime
from django.db import models



class School(models.Model):
    """ 学校 """
    name = models.CharField(max_length=32,verbose_name='学校名字')
    address = models.CharField(max_length=100,verbose_name='学校地址')
    #date = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间', null=True, blank=True)
    num = models.IntegerField(verbose_name='建校时间', blank=True, null=True)
    per = models.IntegerField(verbose_name='高考升学率', blank=True, null=True)
    
    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Blog(models.Model):  
    name = models.CharField(verbose_name="博客名称", max_length=100)  
    tagline = models.TextField(verbose_name="博客标语")  
    def __str__(self):              
        return self.name  
      
class Author(models.Model):  
    name = models.CharField(verbose_name="作者姓名", max_length=50)  
    email = models.EmailField(verbose_name="邮箱",)  
    def __str__(self):             
        return self.name  
       
class Entry(models.Model):  
    blog = models.ForeignKey(Blog, verbose_name="博客名称", on_delete=models.PROTECT, null=True,blank=True)  
    headline = models.CharField(verbose_name="大字标题", max_length=255)  
    body_text = models.TextField(verbose_name="博客内容",)  
    author = models.ManyToManyField(Author)  
    def __str__(self):              
        return self.headline