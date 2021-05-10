from django.db import models
from accounts.models import CustomUser
from subjects.models import Branch,Sem,Course,Subject
# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    sem = models.ForeignKey(Sem,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name + " " +self.user.last_name
    



