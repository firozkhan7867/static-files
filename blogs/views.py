from django.shortcuts import render
from blogs.models import Blog
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  
from teacher.models import Teacher

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,4)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    
    context = {
        'blogs':paged_blogs,
    }
    return render(request,'blogs/blogs.htm',context)

def blog_details(request,name):
    
    blog = get_object_or_404(Blog,name=name)
    
    context = {
        'blog':blog,
    }
    
    return render(request,'blogs/blog-details.htm',context)

def add_blog(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers':teachers,
    }
    return render(request,'admin/user/add_blog.htm',context)

def manage_blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request,'admin/user/manage_blogs.htm',context)





