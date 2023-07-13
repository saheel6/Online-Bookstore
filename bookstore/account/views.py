from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView
from django.urls import reverse_lazy
from .forms import Signupform,signinform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator




# decorators

def signinrequerd(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"sign in requerd")
            return redirect('signinu')
    return inner



# Create your views here.


class Signupview(View):
    def get(self,request,*args,**kwargs):
        Suform=Signupform()
        return render(request,"signup.html",{'sf':Suform})
    def post(self,request,*args,**kwargs):
        form_data=Signupform(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"signin success")
            return redirect('signinu')
        else:
            messages.error(request,"invalid input")
            return redirect('Signupu')
            
        

    

# class Signupview(CreateView):
#     template_name = "signup.html"
#     form_class = Signupform
#     success_urls = reverse_lazy('signinu')


class signinview(View):
    def get(self,reqeust,*args,**kwargs):
        sif=signinform()
        return render(reqeust,'signin.html',{'sif':sif})
    
    def post(self,reqeuest,*args,**kwargs):
        form_data=signinform(data=reqeuest.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user_ob=authenticate(reqeuest,username=uname,password=pswd)
            
            if user_ob:
                login(reqeuest,user_ob)
                messages.success(reqeuest,'login success')
                return redirect('home')
            else:
                messages.error(reqeuest,'input error')
                return redirect('signinu')
            
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('signinu')   
