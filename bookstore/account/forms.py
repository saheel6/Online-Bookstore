from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Signupform(UserCreationForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control custom-field"}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control custom-field"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control custom-field"}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control custom-field"}))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control custom-field"}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control custom-field"}))


    class meta():
        model=User

        fields={'first_name','last_name','email','username','password1','password2'}



class signinform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"username","class":"form-control custom-field"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"password","class":"form-control custom-field"}))
        

     