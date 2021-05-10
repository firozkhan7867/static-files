from django.urls import path
from . import views
urlpatterns = [
    path('blogs',views.blogs,name="blogs"),
    path('blog-details/<str:name>',views.blog_details,name="blog-details"),
    path('admin/add-blog/',views.add_blog,name="add-blog"),
    path('admin/manage-blog/',views.manage_blog,name="manage-blog"),
]
