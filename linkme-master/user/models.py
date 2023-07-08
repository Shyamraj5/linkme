from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="Profile")
    user_name=models.CharField(max_length=200)
    bio=models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='Dp' )
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("other","other")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    def __str__(self):
        return self.user.username
    
class Posts(models.Model):
    Image=models.ImageField(upload_to="post_img",null=True)
    caption=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user")
    likes=models.ManyToManyField(User,related_name="liked_user")