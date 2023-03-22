from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
# from django.db import transaction

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={ 
                "class" : "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",'placeholder' : "Username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",'placeholder' : "First Name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",'placeholder' : "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control",'placeholder' : "Set Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control",'placeholder' : "Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2','is_admin']

    # def save(self,commit=True):
    #     user = super(SignUpForm,self).save(commit=False)
    #     user.is_admin = True

    #     if commit:
    #         user.save()
    #         user1 = User.objects.create(user=user)
    #         user1.save()


class SignUpFormD(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",'placeholder' : "Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",'placeholder' : "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control",'placeholder' : "Set Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control",'placeholder' : "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_pmanager','is_teamleader','is_developer','is_tester')
