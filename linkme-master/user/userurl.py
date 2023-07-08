from django.urls import path
from .views import *

urlpatterns = [
    path("Home/",UserHome.as_view(),name='Homepage'),
]
