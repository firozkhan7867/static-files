# Generated by Django 3.1.1 on 2021-05-03 03:58

from django.db import migrations, models
import subjects.models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20210502_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_img',
            field=models.ImageField(blank=True, upload_to=subjects.models.path_and_rename_course, verbose_name='Course Pic'),
        ),
    ]
