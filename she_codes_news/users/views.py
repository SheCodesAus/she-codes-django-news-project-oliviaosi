from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import CustomUser
from news.models import NewsStory


# Create your views here.

# from django.urls import reverse_lazy

# from news.forms import StoryForm


class UserProfileView(generic.DetailView):

    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name= 'currentuser'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.request.user.id)
        # context['all_stories'] = NewsStory.objects.all()
        return context
   
  
    def get_object(self):
        return self.request.user


#get user object based on username

# from django.shortcuts import get_object_or_404
# from django.views.generic import DetailView

# class Profile(DetailView):

#       template_name = 'users/authorProfile.html'
#       queryset = CustomUser.objects.all()

#       def get_object(self):

#            UserName= self.kwargs.get("username")
#            return get_object_or_404(CustomUser, username=UserName)



