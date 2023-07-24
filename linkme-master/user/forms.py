from django import forms
from . models import *


class Profileform(forms.ModelForm):
    class Meta:
        model=Profile

        exclude = ["user","folower"]
        Widgets={
            "bio":forms.TextInput(attrs={"class":"form-control","type":"textarea"}),
            "image":forms.FileInput()
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["Image","caption"]
        widgets={
            "Image":forms.FileInput(),
            "caption":forms.TextInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields =["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"}),
        }
class UserSearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class CPForm(forms.Form):
    cp=forms.CharField(max_length=100,label="Current Password",widget=forms.PasswordInput)
    np=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput)
    cnp=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput)


