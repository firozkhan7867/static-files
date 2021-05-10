from django.shortcuts import render
from .models import Teacher
from django.shortcuts import get_object_or_404
from subjects.models import Course,Branch,Subject
# Create your views here.
def add_teacher(request):
    branches = Branch.objects.all()
    courses = Subject.objects.all()
    context = {
        "branchs":branches,
        "courses":courses,
    }
    return render(request,'admin/user/add_teacher.htm',context)

def manage_teacher(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers":teachers,
    }
    return render(request,'admin/user/manage_teacher.htm',context)


def edit_teacher(request,username):
    teacher = get_object_or_404(Teacher,username=username)
    branches = Branch.objects.all()
    courses = Subject.objects.all()
    context = {
        "branchs":branches,
        "courses":courses,
        "teacher":teacher,
    }
    return render(request,'admin/user/edit_teacher.htm',context)





