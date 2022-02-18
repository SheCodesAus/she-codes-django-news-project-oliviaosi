# from socket import fromshare
from django import forms

from django.forms import ModelForm
from .models import NewsStory
from .models import NewAuthor

class StoryForm(ModelForm):
    class Meta:
        model= NewsStory
        fields = ['title','pub_date','content','image']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
        attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        }
    # fields = ['title','author','pub_date','content','image']

class AuthorForm(ModelForm):
    class Meta:
        model= NewAuthor
        fields = ['user_name','password','confirm_password']
        