from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm, SignUpFormD
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import admin_required,pmanager_required
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.core.mail import send_mail
from .models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context = {'form' : form}
        if form.is_valid():
            user = form.save()
            created = True
            print(created)
            login(request,user)
            context = {'created' : 'created'}
            return redirect('login_view')
        else:
            return render(request, 'signup.html',context)
        
    else:
        form = SignUpForm()
        context = {
            'form' : form,
        }
        return render(request, 'signup.html', context)

def signup_viewd(request):
    msg = None
    if request.method == 'POST':
        form = SignUpFormD(request.POST)
        context = {'form' : form}
        if form.is_valid():
            user = form.save()
            created = True
            # print(created)
            login(request,user)
            context = {'created' : 'created'}
            return redirect('login_view')
        else:
            return render(request, 'signupd.html',context)
        
    else:
        form = SignUpFormD()
        context = {
            'form' : form,
        }
        return render(request, 'signupd.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username= username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'error validating form'
    return render(request, 'loginindex.html', {'form' : form, 'msg' : msg})


# class LoginView(LoginView):
    
#     template_name = 'user/login.html'
    
#     def get(self, request, *args, **kwargs):
#         print(self.request.user)
#         # if self.request.user.is_teacherrr:
#         #     print('teacher')
#         # else:
#         #     print('student')    
#         return self.render_to_response(self.get_context_data())
    
#user email -->
def sendMail(mailid):
    subject = 'Welcome to Project Management System'
    message = 'Thank you for registering with us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mailid]
    res = send_mail(subject, message, email_from, recipient_list)
    # print(res)
    return res





@admin_required
@login_required(login_url='loginindex.html')
def home(request):
    return render(request,'Homeindex.html')

# @pmanager_required
# @login_required
# def managerhome(request):