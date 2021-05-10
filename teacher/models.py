from django.db import models
from subjects.models import Subject,Branch,Course,Sem,SubjectDescription
from ckeditor.fields import RichTextField
from datetime import datetime
import os
# Create your models here.

# important functions to change filename to store
def path_and_rename_teacher(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]

    if instance.username:
        filename = f"Faculty/{instance.username}/{instance.username}.{ext}"
    return os.path.join(upload_to, filename)



class Teacher(models.Model):
    username = models.CharField(max_length=200,unique=True)
    first_name = models.CharField(max_length=200,blank=True)  
    last_name = models.CharField(max_length=200,blank=True) 
    email = models.EmailField(max_length=200,unique=True) 
    profile_photo = models.ImageField(
        upload_to=path_and_rename_teacher, verbose_name="Faculty Pic")
    department = models.ForeignKey(Branch,on_delete=models.CASCADE)
    experience = models.IntegerField()
    languages = models.CharField(max_length=100)
    about = RichTextField()
    qualification = RichTextField()
    courses = models.ManyToManyField(Subject)
    address = models.CharField(max_length=200,blank=True)
    date_joined = models.DateTimeField(default=datetime.now,blank=True)
    
    facebook_link = models.CharField(max_length=100,blank=True)
    twitter_link = models.CharField(max_length=100,blank=True)
    linkedin_link = models.CharField(max_length=100,blank=True)
    instagram_link = models.CharField(max_length=100,blank=True)
    
    programming_skills = models.IntegerField()
    communication_skills = models.IntegerField()
    teching_skills = models.IntegerField()
    achievements  = RichTextField(blank=True,null=True)
    
    
    def __str__(self):
        return self.username








