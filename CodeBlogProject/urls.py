
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members', include('django.contrib.auth.urls')),
    path('members', include('members.urls')),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),

]
