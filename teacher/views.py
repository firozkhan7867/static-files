from django.shortcuts import render
from .models import Teacher
from django.shortcuts import get_object_or_404
from subjects.models import Course,Branch
# Create your views here.
def teachers(request):
    teacher = Teacher.objects.all()
    context = {
        'teachers':teacher,
    }
    return render(request,'teacher/teacher_page.htm',context)

def teacher_details(request,username):
    teacher = get_object_or_404(Teacher,username=username)
    courses = teacher.courses.all()
    
    
    for i in courses:
        # for i in course.subject.teacher_set.all():
        print(i.teacher_set.all())
        
    # print(courses)
    # courses = SubjectDescription.objects.all().filter(subject=teacher.courses.subject_id)
    # print(courses)
    context = {
        'teacher':teacher,
        'courses':courses,
    }
    return render(request,'teacher/teacher_details.htm',context)


