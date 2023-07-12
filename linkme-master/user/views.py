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
from django.utils.decorators import method_decorator

#==== Decorator ====#
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect ("Homepage")
    return wrapper

@method_decorator(signin_required,name='dispatch')
class UserHome(CreateView):
    template_name="home.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("Homepage")
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,'Post Uploaded')
        self.object=form.save()
        return super().form_valid(form)
       
    def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context["Feed"]=Posts.objects.all()
            context['cform']=CommentForm()
            context["comments"]=Comments.objects.all()
            return context
    
def addcomment(request,*args,**kwargs):
    if request.method=="POST":
        cid=kwargs.get("cid")
        post=Posts.objects.get(id=cid)
        user=request.user
        cmnt=request.POST.get("comment")
        Comments.objects.create(comment=cmnt,user=user,post=post)
        return redirect ("Homepage")

     

@method_decorator(signin_required,name='dispatch')
class DeletePost(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("eid")
        post=Posts.objects.get(id=eid)
        post.delete()
        return redirect('Homepage')
    
@method_decorator(signin_required,name='dispatch')
class ProfileEdit(CreateView):
    form_class=Profileform
    template_name="setting.html"
    model=Profile
    success_url=reverse_lazy("Homepage")
    
    def form_valid(self,form1):
        form1.instance.user=self.request.user
        self.object = form1.save()
        messages.success(self.request,"Bio Added")
        return super().form_valid(form1)
    
    
@method_decorator(signin_required,name='dispatch')
class ProfileView(CreateView):
    form_class=Profileform
    template_name="profile.html"
    model=Profile
    success_url=reverse_lazy("Homepage")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object = form.save()
        print("saved")
        messages.success(self.request,"Profile Updated")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
          
            context=super().get_context_data(**kwargs)
            context["posts"]=Posts.objects.filter(user=self.request.user)
            context["follow"]= Profile.objects.all()
            
            return context
    
def following(req,*args, **kwargs):
    fid=kwargs.get("fid")
    post=Profile.objects.get(id=fid)
    user=req.user
    post.folower.add(user)
    post.save()
    return redirect ("Homepage")

# def profile2(request):
#         user = request.user
#         posts = Posts.objects.filter(user=user).order_by('-timestamp')
#         return render(request, 'profile.html', {'posts': posts})


def addlike(req,*args, **kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid)
    user=req.user
    post.likes.add(user)
    post.save()
    return redirect ("Homepage")

@method_decorator(signin_required,name='dispatch')
class BioEdit(UpdateView):
    form_class=Profileform
    model=Profile
    template_name="setting.html"
    success_url=reverse_lazy("vp")
    pk_url_kwarg="id"


# class BioEdit(View):
#     def get(self,request,*args, **kwargs):
#         id=kwargs.get("eid")
#         man=Posts.objects.get(id=id)
#         form=PostForm(instance=man)
#         return render(request,'setting.html',{"datas":form})
#     def post(self,request,*args, **kwargs):
#         id=kwargs.get("eid")
#         man=DeletePost.objects.get(id=id)
#         form_pdata=PostForm(request.POST,instance=man,files=request.FILES )
#         if form_pdata.is_valid():
           
#             man.save()
#             messages.success(request,'manager updated successfully')
#             return redirect("pr")
#         else:
#             return render(request,"profile.html",{"datas":form_pdata})

# def addfollow(req,*args, **kwargs):
#     fid=kwargs.get("fid")
#     follow=Profile.objects.get(id=fid)
#     user=req.user
#     follow.follower.add(user)
#     follow.save()
#     return redirect ("Homepage")

# def followers(request):
#     profile = Profile.objects.get(user=request.user)
#     followers = profile.all()
#     followers_count = profile.followers_count()
#     return render(request, 'followers.html', {'followers': followers, 'followers_count': followers_count})



class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect("home")