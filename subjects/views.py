from django.shortcuts import render,redirect
from student.models import Student
from .models import Branch,Course,Sem,Subject,SubjectDescription
from teacher.models import Teacher
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator    
# Create your views here.



def start(request):
    return redirect('index')

def index(request):
    
    branchs = Branch.objects.all()
    sub = SubjectDescription.objects.all()
    # subj= Subject.objects.get(subject_id=5)
    teacher = Teacher.objects.all()
    
    
    
    # for i in sub:
    #     print(i.subject.teacher.username)
    
    
    branch_list = [i for i in branchs]
    cse = branch_list[0]
    mech = branch_list[1]
    civil = branch_list[2]
    ece = branch_list[3]
    eee = branch_list[4]
    it = branch_list[5]
    
    context = {
        'branch':branchs,
        'cse':cse,
        'mech':mech,
        'civil':civil,
        'ece':ece,
        'eee':eee,
        'it':it,
        'subs': sub,
        'teachers':teacher,
    }
    
    
    return render(request,'main/index.htm',context)


def about(request):
    return render(request,'main/about.htm')


def courses(request):
    sub = SubjectDescription.objects.all()
    
    paginator = Paginator(sub,6)
    page = request.GET.get('page')
    paged_sub = paginator.get_page(page)
    
    context = {
        'subs':paged_sub
    }
    return render(request,'main/courses.htm',context)


def cousre_details(request,subject_name):
    sub = get_object_or_404(Subject,subject_name=subject_name)
    # sub = Subject.objects.get(subject_name=subject_name)
    
    sub_desc = SubjectDescription.objects.get(subject=sub.subject_id)
    
    context = {
        'sub':sub_desc,
    }
    if sub.chapter.all():
        chapters = sub.chapter.all()
        context['chapters'] = chapters
    else:
        context['chapters'] = None
    
    return render(request,'main/course_details.htm',context)


def course(request,branch_name):
    branch = get_object_or_404(Branch,branch_name=branch_name)
    course_list = [i for i in branch.course.all()]
    btech = course_list[0]
    mtech = course_list[1]
    diploma = course_list[2]
    try:
        degree = course_list[3]
    except:
        degree = None
    context = {
        'btech':btech,
        'mtech':mtech,
        'diploma':diploma,
        'degree':degree,
        'branch_name':branch_name,
    }
    
    return render(request,'course/course.htm',context)



def sem_list(request,branch_name,course_name):
    
    if request.method == 'POST':
        sem = request.POST.get('sem')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        sub = Subject.objects.all().filter(sem=sem,course=course,branch=branch)
        branch = get_object_or_404(Branch,branch_name=branch_name)
        course = branch.course.get(course_name=course_name)
        sems = course.sem.all()
        current_sem = course.sem.get(sem_id=sem)
        
        paginator = Paginator(sub,2)
        page = request.GET.get('page')
        paged_sub = paginator.get_page(page)
        
        context = {
            'subs':paged_sub,
            'sem_list':sems,
            'course':course,
            'branch':branch,
            'current_sem':current_sem,
        }
        return render(request,'course/sem_list.htm',context)
    
    
    branch = get_object_or_404(Branch,branch_name=branch_name)
    course = branch.course.get(course_name=course_name)
    sem = course.sem.all()
    sub = Subject.objects.all().filter(branch=branch,course=course)
    paginator = Paginator(sub,2)
    page = request.GET.get('page')
    paged_sub = paginator.get_page(page)
        
    
    context = {
        'sem_list':sem,
        'course':course,
        'branch':branch,
        'subs':paged_sub,
    }
    
    
    return render(request,'course/sem_list.htm',context)



def add_subject(request):
    branchs = Branch.objects.all()
    courses = Course.objects.all()
    sems = Sem.objects.all()
    teachers = Teacher.objects.all()
    
    context = {
        "branchs":branchs,
        "courses":courses,
        "sems":sems,
        "teachers":teachers,
    }
    return render(request,'admin/user/add_subject.htm',context)

def manage_subject(request):
    subs = Subject.objects.all()
    context = {
        'subs':subs,
    }
    return render(request,'admin/user/manage_subject.htm',context)

def edit_subject(request,subject_name):
    sub = get_object_or_404(Subject,subject_name=subject_name)
    branchs = Branch.objects.all()
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    sems = Sem.objects.all()
    
    context = {
        'sub':sub,
        "branchs":branchs,
        "courses":courses,
        "teachers" :teachers,
        "sems":sems,
    }    
    return render(request,'admin/user/edit_subject.htm',context)