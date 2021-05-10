from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('subjects.urls')),
    path('teacher/',include('teacher.urls')),
    path('blogs/',include('blogs.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
