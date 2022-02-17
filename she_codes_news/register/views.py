# from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import RegisterUser
from .form import RegisterUserForm
from users.models import CustomUser
from users.forms import CustomUserCreationForm


# Create your views here.
# def register(response):
#     form= UserCreationForm()
#     return render(response,"register/register.html",{"form":form})


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    context_object_name = 'registerForm'
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')

    # success_url = reverse_lazy('news:index')