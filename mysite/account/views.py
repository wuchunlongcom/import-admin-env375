# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse
from django.contrib.auth.decorators import login_required #使用注意在settings.py中设置 LOGIN_URL = '/login/'


# http://localhost:8000/
#@login_required
def index(request):           
    meg = 'hello world!  index0000'
    return render(request, 'account/index.html', context=locals()) 

# http://localhost:8000/index1/
#@login_required
def index1(request):           
    meg = 'hello world!  index1111'
    return render(request, 'account/index.html', context=locals()) 

"""
from account.models import Blog, Author, Entry

# http://localhost:8000/account/index/
def index(request):           
    #详见模板在Entry中读取blog和author的数据
    entrys = Entry.objects.all() 
    return render(request, 'account/index.html', context=locals()) 

# http://localhost:8000/account/test/
def test(request):           
        
    #在Entry中读取blog和author的数据
    entrys = Entry.objects.all()  
    for e in entrys:  
         blog = e.blog  #一对多
         author = e.author.all() #多对多
         print('blog:', blog)
         print('author:', author)
         
    #在Blog中读取Entry
    blogs = Blog.objects.all()
    for blog in blogs:
        entry = blog.entry_set.all()
        print('blog——entry:', entry)
    
    #在Author中读取Entry
    authors = Author.objects.all()
    for author in authors: 
        entry = author.entry_set.all()    
        print('author——entry:', entry)

    return HttpResponse('ok!')
"""

   