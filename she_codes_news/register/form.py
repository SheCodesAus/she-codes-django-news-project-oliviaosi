from django import forms

from django.forms import ModelForm
from .models import RegisterUser

class RegisterUserForm(ModelForm):
    class Meta:
        model= RegisterUser
        fields = ['title','author','pub_date','content','image']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
        attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        }