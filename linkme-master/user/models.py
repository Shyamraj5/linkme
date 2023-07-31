from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="Profile")
    bio=models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='Dp' )
    folower=models.ManyToManyField(User,related_name="follow")

    def __str__(self) -> str:
        return self.bio

    @property
    def allfollower(self):
        print(self.folower.count())
        return self.folower.count()
    @property
    def followeduser(self):
        fl=self.folower.all()
        users=[u.username for u in fl]
        return users

    def __str__(self):
        return self.user
    
class Posts(models.Model):
    Image=models.ImageField(upload_to="post_img",null=True)
    caption=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user")
    likes=models.ManyToManyField(User,related_name="liked_user")
    DP = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="user_dp",null=True)
   
    
    @property
    def allikes(self):
        return self.likes
    
    def likeduser(self):
        lk=self.likes.all()
        users=[u.username for u in lk]
        return users

class Comments(models.Model):
    comment=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment_user")
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="commented_post")


class Favposts(models.Model):
    fav=models.ForeignKey(Posts,on_delete=models.CASCADE, related_name="favo",)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="uuser",null=True)


