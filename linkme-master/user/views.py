from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from django.contrib.auth import logout,authenticate
from django.contrib.auth.views import PasswordChangeView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


class UserHome(CreateView):
    template_name="home.html"
    form_class=Profileform
    model=Profile
    success_url=reverse_lazy("Homepage")