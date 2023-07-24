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
    path("addfav/<int:id>",addfav,name="addfav"),
    path("follow/<int:fid>",following,name="follow"),
    path("myfav/",Fav_list.as_view(),name="favv"),
    path("cha/",ChangePassword.as_view(),name='change'),
    path('delcart/<int:id>',Delfav,name="delfav")

    
   


]
