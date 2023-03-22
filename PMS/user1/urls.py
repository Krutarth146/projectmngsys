from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.core.mail import send_mail
# from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('login/',views.login_view,name='login_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('signupd/',views.signup_viewd,name='signup_viewd'),
    path('home/',views.home,name='home'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('sendmail/',views.sendMail,name='sendmail'),
]