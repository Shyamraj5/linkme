from django import forms
from . models import *


class Profileform(forms.ModelForm):
    class Meta:
        model=Profile

        exclude = ["user"]
        widjets={
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