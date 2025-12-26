"""
URL configuration for todo_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', lambda request: HttpResponseRedirect('/api/')),
]

