from django.urls import path

from . views import  *

urlpatterns = [
    path("Home/",UserHome.as_view(),name='Homepage'),
    path("de/",ProfileEdit.as_view(),name='pr'),
    path("DelPost/<int:eid>",DeletePost.as_view(),name="DelPost"),
    path("ViewP/",ProfileView.as_view(),name='vp'),
    path("liked/<int:pid>",addlike,name="like"),
    path("EditBio/<int:id>",BioEdit.as_view(),name="EditBio"),
    path("Comment/<int:cid>",addcomment,name="cmnt"),
    path("logout/",LogOut.as_view(),name='logout'),
    
    # path("liked/<int:fid>",addfollow,name="follow"),


]
