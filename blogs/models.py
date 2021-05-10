from django.db import models
from accounts.models import CustomUser
from teacher.models import Teacher
from student.models import Student
from datetime  import datetime
from ckeditor.fields import RichTextField
import os
# Create your models here.



def path_and_rename_blog(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]

    if instance.name:
        filename = f"Blog/{instance.name}/{instance.name}.{ext}"
    return os.path.join(upload_to, filename)

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=200,unique=True)
    date_upload = models.DateTimeField(default=datetime.now,blank=True)
    # category
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUser)
    main_photo = models.ImageField(
        upload_to=path_and_rename_blog, verbose_name="Blog Pic",blank=True)
    main_photo_1 = models.ImageField(
        upload_to=path_and_rename_blog, verbose_name="Blog Pic",blank=True)
    main_photo_2 = models.ImageField(
        upload_to=path_and_rename_blog, verbose_name="Blog Pic",blank=True)
    
    description = RichTextField()
    short_description = RichTextField(blank=True,null=True)
    description_2 = RichTextField(blank=True,null=True)
    description_3 = RichTextField(blank=True,null=True)
    
    # tags
    # likes
    # comments
    # source
    
    def __str__(self):
        return self.name