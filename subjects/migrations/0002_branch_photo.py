# Generated by Django 3.1.1 on 2021-05-02 03:33

from django.db import migrations, models
import subjects.models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='photo',
            field=models.ImageField(blank=True, upload_to=subjects.models.path_and_rename_branch, verbose_name='Branch Pic'),
        ),
    ]
