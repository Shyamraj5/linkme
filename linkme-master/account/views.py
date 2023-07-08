from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.
class Login(FormView):
    template_name="signin.html"
    form_class=LoginForm
    def post (self,req,*args,**kwargs):
        form_data=LoginForm(data=req.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            psw=form_data.cleaned_data.get("password")
            user=authenticate(req,username=un,password=psw)
            if user:
                print(user.first_name,user.last_name)
                login(req,user)
                messages.success(req,"LOgin SucCess")
                return redirect("Homepage")
            else:
                messages.error(req,"Login Failed")
                return redirect("home")
        else:
            return render (req,"Homepage.html",{"form":form_data})


class SignUp(CreateView):
    form_class=RegistrationForm
    template_name="signup.html"
    model=User
    success_url=reverse_lazy("home")