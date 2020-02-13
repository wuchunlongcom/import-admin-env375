# -*- coding: utf-8 -*-
from django.db import models




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