from typing import Any, Dict
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView,ListView
from django.contrib.auth import logout,authenticate
from django.contrib.auth.views import PasswordChangeView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

#==== Decorator ====#
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect ("Homepage")
    return wrapper
dec=[signin_required,never_cache]

@method_decorator(dec,name='dispatch')
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

     

@method_decorator(dec,name='dispatch')
class DeletePost(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("eid")
        post=Posts.objects.filter(id=eid,user=self.request.user)
        post.delete()
        return redirect('Homepage')
    
@method_decorator(dec,name='dispatch')
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
     
    
    
@method_decorator(dec,name='dispatch')
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
            context["postsc"]=Posts.objects.filter(user=self.request.user).count()
            context["pro"]=Profile.objects.get(user=self.request.user)
            
            
            return context
     

    
def following(req,*args, **kwargs):
    fid=kwargs.get("fid")
    post=Profile.objects.get(id=fid)
    
    user=req.user
    post.folower.add(user)
    # post.save()
    return redirect ("Homepage")



def addlike(req,*args, **kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid)
    user=req.user
    post.likes.add(user)
    post.save()
    return redirect ("Homepage")

 

  


@method_decorator(dec,name='dispatch')
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

#search


class search(TemplateView):
    template_name="search.html"

class ChangePassword(FormView):
    form_class=CPForm
    template_name="changepass.html"
    def post(self,req,*args, **kwargs):
        form_data=CPForm(data=req.POST)
        if form_data.is_valid():
            current=form_data.cleaned_data.get("cp")
            new=form_data.cleaned_data.get("np")
            confirm=form_data.cleaned_data.get("cnp")
            print(current)
            user=authenticate(req,username=req.user.username,password=current)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    messages.success(req,"Password Changed")
                    logout(req)
                    return redirect('Homepage')
                else:
                    messages.error(req,"Password  mismatched")
                    return redirect("change")
            else:
                messages.error(req,"Incorrect Password")
                return redirect("change")
        else:
            return render(req,"changepass.html",{"form":form_data})

def addfav(request,*args,**kwargs):
    id=kwargs.get("id")
    post=Posts.objects.get(id=id)
    user=request.user
    if Favposts.objects.filter(fav=post,user=user):
        messages.warning(request,"Already Added in favorites")
        return redirect('Homepage')
    else:
        Favposts.objects.create(fav=post,user=user)
        messages.success(request,"added o favourates")
        return render(request,"fav.html")
def Delfav(request,*args,**kwargs):
        id=kwargs.get("id")
        Favposts.objects.filter(id=id).delete()
        messages.success(request,"item removed")
        return redirect("favv")


def fav_list(request,**kwargs):
    
    fav = Favposts.objects.get(id=1)  # Replace 1 with the actual cart ID
  

    return render(request, 'fav.html', {'favv': fav})



class Fav_list(TemplateView):
    template_name="fav.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["fav"]=Favposts.objects.filter(user=self.request.user)
        
        return context
    
class userprofiles(TemplateView):
   template_name="userprofileview.html"
   def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
       id=kwargs.get("id")
       context= super().get_context_data(**kwargs)
       context["post"]=Posts.objects.filter(user=id)
       context["pro"]=Profile.objects.get(user=id)
       
       return context
  
       
       
       

    



class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect("home")