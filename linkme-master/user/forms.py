from django import forms
from . models import *


class Profileform(forms.ModelForm):
    class Meta:
        model=Profile

        exclude = ["user"]
        widjets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "bio":forms.TextInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "image":forms.FileInput()
            

        }