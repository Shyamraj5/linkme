from django.urls import path

from . views import  *

urlpatterns = [
    path("Home/",UserHome.as_view(),name='Homepage'),
    path("de/",Profile.as_view(),name='pr'),
    path("DelPost/<int:eid>",DeletePost.as_view(),name="DelPost"),
    path("ViewP/",ProfileView.as_view(),name='vp'),
    path("liked/<int:pid>",addlike,name="like"),

]
