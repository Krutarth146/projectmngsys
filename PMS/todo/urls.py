from django.contrib import admin
from django.urls import path,include
# from .views import 
from django.contrib.auth.views import LogoutView
from .views import CreateProject, ListAllProject

urlpatterns = [
    path('create/',CreateProject.as_view(),name='create'),
    path('list/',ListAllProject.as_view(),name='list'),
]