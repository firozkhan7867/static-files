from django.urls import path
from . import views
urlpatterns = [
    path('',views.start,name="start"),
    path('index',views.index,name="index"),
    path('about',views.about,name="about"),
    path('courses',views.courses,name="courses"),
    path('course-details/<str:subject_name>/',views.cousre_details,name="course-details"),
    path("Branch/<str:branch_name>/",views.course,name="branch-courses"),
    path('Branch/<str:branch_name>/<str:course_name>/',views.sem_list,name="sem-list"),
    path('Admin/add-subject/',views.add_subject,name="add-subject"),
    path('Admin/manage-subject/',views.manage_subject,name="manage-subject"),
    path('Admin/edit-subject/<str:subject_name>',views.edit_subject,name="edit-subject"),
]
