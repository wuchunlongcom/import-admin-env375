# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import  School, Blog, Author, Entry

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export.resources import ModelResource


@admin.register(School)
class SchoolAdmin(ImportExportMixin, admin.ModelAdmin):    
    #list_display = ('id','name','address','date','num','per')
    list_display = ('id','name','address','num','per')



class BlogResource(ModelResource):

    class Meta:
        model = Blog

#     def for_delete(self, row, instance):
#         return self.fields['name'].clean(row) == ''


@admin.register(Blog)
class BlogAdmin(ImportExportMixin, admin.ModelAdmin):    
    list_display = ('id','name','tagline')
    resource_class = BlogResource
  
    
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
        
