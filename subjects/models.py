from django.db import models
import os
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.



# important functions to change filename to store
def path_and_rename_subj(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]

    if instance.subject_name:
        filename = f"Subjects/{instance.subject_name}/{instance.subject_name}.{ext}"
    return os.path.join(upload_to, filename)

def path_and_rename_branch(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]

    if instance.branch_name:
        filename = f"Branch/{instance.branch_name}/{instance.branch_name}.{ext}"
    return os.path.join(upload_to, filename)

def path_and_rename_course(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]

    if instance.course_name:
        filename = f"Branch/{instance.course_name}/{instance.course_name}.{ext}"
    return os.path.join(upload_to, filename)

def path_and_rename_chapter(instance, filename):
    upload_to = "PDF/"
    ext = filename.split('.')[-1]

    if instance.chapter_name:
        filename = f"Subject/{instance.chapter_name}/{instance.chapter_name}.{ext}"
    return os.path.join(upload_to, filename)



class Sem(models.Model):
    sem_id = models.AutoField(primary_key=True)
    sem_name = models.CharField(max_length=100,blank=False)
    
    def __str__(self):
        return self.sem_name
    
class Course(models.Model):
    couse_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=40,blank=False)
    sem = models.ManyToManyField(Sem)
    course_img = models.ImageField(
        upload_to=path_and_rename_course, verbose_name="Course Pic",blank=True)
    course_img_2 = models.ImageField(
        upload_to=path_and_rename_course, verbose_name="Course Pic",blank=True)
    course_img_3 =  models.ImageField(
        upload_to=path_and_rename_course, verbose_name="Course Pic",blank=True)
    
    def __str__(self):
        return self.course_name
    

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=50,blank=True)
    course = models.ManyToManyField(Course)
    photo = models.ImageField(
        upload_to=path_and_rename_branch, verbose_name="Branch Pic",blank=True)
    photo_2 = models.ImageField(
        upload_to=path_and_rename_branch, verbose_name="Branch Pic",blank=True)
    photo_3 = models.ImageField(
        upload_to=path_and_rename_branch, verbose_name="Branch Pic",blank=True)
    
    
    def __str__(self):
        return self.branch_name
    
    
    
class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter_name = models.CharField(unique=True,db_index=True,max_length=300)
    pdf_material = models.FileField(
        upload_to=path_and_rename_chapter,blank=True)
    pdf_material_1 = models.FileField(
        upload_to=path_and_rename_chapter,blank=True)
    pdf_material_2 = models.FileField(
        upload_to=path_and_rename_chapter, blank=True)
    pdf_material_3 = models.FileField(
        upload_to=path_and_rename_chapter,blank=True)
    pdf_link = models.URLField(max_length=500,null=True,blank=True)
    video_link = models.URLField(max_length=500,null=True,blank=True)
    question_papers = models.URLField(max_length=500,null=True,blank=True)
    topics = RichTextField(null=True,blank=True)
    
    def __str__(self):
        return self.chapter_name
    
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200,blank=False)
    sem = models.ManyToManyField(Sem)
    course = models.ManyToManyField(Course)
    branch = models.ManyToManyField(Branch)
    chapter = models.ManyToManyField(Chapter)
    
    
    
    subj_image = models.ImageField(
        upload_to=path_and_rename_subj, verbose_name="Subject Pic")
    subj_image_2 = models.ImageField(
        upload_to=path_and_rename_subj, verbose_name="Subject Pic2",blank=True)
    subj_image_3 = models.ImageField(
        upload_to=path_and_rename_subj, verbose_name="Subject Pic3",blank=True)
    
    
    
    def __str__(self):
        return self.subject_name
    


class SubjectDescription(models.Model):
    subject = models.OneToOneField(Subject,on_delete=models.CASCADE)
    
    
    description_1 = RichTextField(blank=False,null=False)
    description_2 = RichTextField(blank=False,null=False)
    description_3 = RichTextField(blank=True,null=True)
    
    # instructor = ""
    # reviews 
    # view count = 
    upload_date = models.DateTimeField(default=datetime.now,blank=True)
    # price
     
    
    def __str__(self):
        return self.subject.subject_name    




    
    














