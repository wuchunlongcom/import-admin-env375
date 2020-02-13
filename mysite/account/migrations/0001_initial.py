# Generated by Django 2.2.6 on 2020-02-13 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='作者姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='博客名称')),
                ('tagline', models.TextField(verbose_name='博客标语')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='大字标题')),
                ('body_text', models.TextField(verbose_name='博客内容')),
                ('author', models.ManyToManyField(to='account.Author')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.Blog', verbose_name='博客名称')),
            ],
        ),
    ]
