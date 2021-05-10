from django.urls import path
from . import views
from . import admin_views
urlpatterns = [
    path('teachers',views.teachers,name="teachers"),
    path('teacher-details/<str:username>/',views.teacher_details,name='teacher-details'),
    path('admin/add-teacher/',admin_views.add_teacher,name="add-teacher"),
    path('admin/manage-teachers/',admin_views.manage_teacher,name="manage-teacher"),
    path('admin/edit-teachers/<str:username>/',admin_views.edit_teacher,name="edit-teacher"),
]
