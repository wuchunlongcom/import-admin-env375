# -*- coding: UTF-8 -*-
import os
import sys
import django
import random

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission
    
    #组添加权限 django==2.2.6 通用
    operatorGroup = Group.objects.create(name='Operator')
    operatorGroup.permissions.add(
        #Permission.objects.get(name='Can add blog'),
              
    )
    operatorGroup.save()
    
    customerGroup = Group.objects.create(name='Customer')
    customerGroup.permissions.add()
    customerGroup.save()
        
    # 创建超级用户 admin/admin
    if not User.objects.filter(username = 'admin'):
        User.objects.create_superuser('admin', 'admin@test.com','admin')
     

"""    
    from account.models import Blog, Author, Entry
    blogs = [('命运共同体','构建'), ('中国制度','自我完善'), ('创新发展','制度保障')]
    items = [Blog(name=i[0], tagline=i[1]) for i in blogs]
    Blog.objects.bulk_create(items, batch_size=20)
    
    authors = [('王大勇','a@1.com'), ('许宠名','b@1.com'), 
               ('张信哲','c@1.com'), ('赵力全','d@1.com')]
    
    items = [Author(name=i[0], email=i[1]) for i in authors]
    Author.objects.bulk_create(items, batch_size=20)
    
    entrys = [('人民日报评论部', '为构建人类命运共同体不断作出贡献'),
              ('人民日报人民论坛', '中国制度具有自我完善能力'),
              ('人民日报新知新觉', '推动区块链技术和产业创新发展'),
              ('人民日报', '为加快推动高质量发展提供制度保障'),
              ('人民日报声音', '承担源头责任 拿出干流担当')]
    
    terms = [( Blog.objects.get(name=blogs[random.randint(0,len(blogs)-1)][0]),
              i[0], i[1]) for i in entrys]

    items = [Entry(blog=i[0], headline=i[1], body_text=i[2]) for i in terms]
    Entry.objects.bulk_create(items, batch_size=20)
     
    #多对多 根据headline(大字标题不同)  作者赋值一样   
#     [(e.author.add(Author.objects.get(name = authors[0][0]),
#                    Author.objects.get(name = authors[1][0]),
#                    Author.objects.get(name = authors[2][0]),
#                    Author.objects.get(name = authors[3][0])),e.save())  
#     for e in Entry.objects.all()]

    #多对多 根据headline(大字标题不同)  作者赋值不一样 
    e = Entry.objects.get(headline = entrys[0][0])
    e.author.add(Author.objects.get(name = authors[0][0]),
                 Author.objects.get(name = authors[1][0]),
                 Author.objects.get(name = authors[2][0]),
                 Author.objects.get(name = authors[3][0]))

    e = Entry.objects.get(headline = entrys[1][0])
    e.author.add(Author.objects.get(name = authors[0][0]),
                 Author.objects.get(name = authors[3][0]))
    
    e = Entry.objects.get(headline = entrys[2][0])
    e.author.add(Author.objects.get(name = authors[1][0]))
    
    e = Entry.objects.get(headline = entrys[3][0])
    e.author.add(Author.objects.get(name = authors[0][0]),
                 Author.objects.get(name = authors[2][0]),
                 Author.objects.get(name = authors[3][0]))
    
    e = Entry.objects.get(headline = entrys[4][0])
    e.author.add(Author.objects.get(name = authors[0][0]),
                 Author.objects.get(name = authors[1][0]),
                 Author.objects.get(name = authors[3][0]))
    
"""
