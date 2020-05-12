python3.7.5   django2.2.6  部署正常                      

### 功能：使用django-import-export  admin具有导入和导出数据库的数据功能。 
支持中文导入excel
存在问题：有日期字段时导入excel错误！2020.05.12

      
```
一、 运行      
1、运行：./start.sh 

二、 后台超级用户登录
用户名/密码  
admin/admin

三、用户登录
http://localhost:8000/
```

```
import-admin
注意：1、上传git, 删除env375；
     2、./start.sh -i   要保证env375在工程中；
     3、本工程的 env375与requirements.txt 必须配合使用；
     4、一个工程一个虚拟环境是必须的，否则容易产生本机运行正常，部署却不正常的问题。
```


```
参考文档：
excel 文件的导入
https://www.cnblogs.com/yjlch1016/archive/2019/08/18/11373785.html   # ok
python mysite/manage.py collectstatic
此时static目录下新增了static/import_export目录  

```

```
使用其中模块 https://github.com/django-import-export/django-import-export           
django-import-export库支持多种格式，包括xls、csv、json、yaml以及tablib支持的所有其他格式。      

参考： https://django-import-export.readthedocs.io/en/latest/index.html       
```