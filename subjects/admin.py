from django.contrib import admin
from .models import Course,Sem,Subject,Branch,SubjectDescription,Chapter
# Register your models here.

admin.site.register([Course,Sem,Subject,Branch,SubjectDescription,Chapter])