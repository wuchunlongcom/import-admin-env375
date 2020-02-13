# -*- coding: utf-8 -*-
from django.contrib import admin



from .models import  Blog, Author, Entry
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):    
    list_display = ('id','name','tagline')
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):    
    list_display = ('id','name','email')
    
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):    
    list_display = ('id','blog','headline','body_text','author_list')
    def author_list(self, entry):
        '''多对多字段'''
        return ','.join([i.name for i in entry.author.all()])
        #names = map(lambda x: x.name, entry.author.all())
        #return ', '.join(names)
        
