from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from subjects.models import Branch,Course,Sem,Subject
from student.models import Student
import os

# Create your views here.




def index(request):
    if request.user.is_authenticated:
        
        
        stud = Student.objects.all().filter(course=1)
        for i in stud:
            print(i,"----------------------")
            
        sub = Subject.objects.order_by('subject_name').filter(branch=3,sem=request.user.student.sem)
        for i in sub:
            print(i,"  --   --   --")
        
            
        
        
        
        user = request.user
        user1 = user.student.sem.sem_name
        print(user1)
        return HttpResponse(f"""<h1>UserName :{user.username}</br> 
                                First_Name:  {user.first_name} </br>
                                Last_Name: {user.last_name} </br>
                                Email: {user.email}</br>
                                Address: {user.address}</br>
                                Phone : {user.phone} </br>
                                <img src="{ user.photo.url}" width="400">
                                {user.photo.url}
                                <a href="logout">logout</a>
                            """)
    else:
        return HttpResponse("""<h1>Please Log in to view 
                             <a href="login">Login</a></h1>""")


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        sem = request.POST.get('sem')
        branch = request.POST.get('branch')
        course = request.POST.get('course')
        
        sem1 = Sem.objects.get(sem_id=sem)
        course1 = Course.objects.get(couse_id=course)
        branch1 = Branch.objects.get(branch_id=branch)
        
            

        user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                              email=email, phone=phone, address=address, password=password)
        user.save()
        user = CustomUser.objects.get(email=email)
        if 'photo' in request.FILES: 
            photo = request.FILES['photo']
            user.photo =  photo #path_and_rename(username ,photo)

        stud = Student(user=user,sem=sem1,course=course1,branch=branch1)
        stud.save()
        
        user.save()
        return redirect('login')
    course = Course.objects.all()
    branch = Branch.objects.all()
    sem = Sem.objects.all()
    
    context = {
        'courses':course,
        'sems':sem,
        'branchs':branch
    }
    
    
    
    return render(request, 'login/register.htm',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'login/login.htm')
    
def logout(request):
    auth.logout(request)
    return redirect('index')



def list_user(request):
    users = CustomUser.objects.all()
    context = {
        "students":users,
    }
    return render(request,'admin/user/user_list.htm',context)