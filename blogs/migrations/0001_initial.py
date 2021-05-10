# Generated by Django 3.1.1 on 2021-05-05 08:29

import blogs.models
import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0007_auto_20210502_2142'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('date_upload', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('main_photo', models.ImageField(blank=True, upload_to=blogs.models.path_and_rename_blog, verbose_name='Blog Pic')),
                ('main_photo_1', models.ImageField(blank=True, upload_to=blogs.models.path_and_rename_blog, verbose_name='Blog Pic')),
                ('main_photo_2', models.ImageField(blank=True, upload_to=blogs.models.path_and_rename_blog, verbose_name='Blog Pic')),
                ('description', ckeditor.fields.RichTextField()),
                ('description_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('description_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]