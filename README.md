python3.7.5   django2.2.6  部署正常                      

### 功能：
```
1、使用django-import-export  admin具有导入和导出数据库的数据功能。
支持中文导入excel
存在问题：有日期字段时导入excel错误！2020.05.12

2、用户、组、权限。使用User, Group, Permission
op0/123 Blog、Author、Entry数据库有 查看(view)、创建(add)、更改(change)权限，Blog有删除权限。
cx0/123 Blog、Author、Entry数据库有 查看(view)、创建(add)权限。

3、一对多、多对多数据初始化，写入数据库。    
```
```
一、 运行      
1、运行：./start.sh 

二、 后台超级用户登录
用户名/密码  
admin/admin
op0/123
cx0/123
三、用户登录
http://localhost:8000/
```


```
参考文档：
excel 文件的导入
https://www.cnblogs.com/yjlch1016/archive/2019/08/18/11373785.html   # ok
python mysite/manage.py collectstatic
此时static目录下新增了static/import_export目录  

权限：https://blog.csdn.net/weixin_42134789/article/details/84567337
使用其中模块 https://github.com/django-import-export/django-import-export 
参考： https://django-import-export.readthedocs.io/en/latest/index.html           
django-import-export库支持多种格式，包括xls、csv、json、yaml以及tablib支持的所有其他格式。      
      
```