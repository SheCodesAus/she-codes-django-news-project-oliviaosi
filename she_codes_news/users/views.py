from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import CustomUser


# Create your views here.

# from django.urls import reverse_lazy
# from news.models import NewsStory
# from news.forms import StoryForm


class UserProfileView(generic.DetailView):

    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name= 'currentuser'

   
    # def currentuser(response):
    #     return render(response,"users/userProfile.html")
    def get_object(self):
        return self.request.user