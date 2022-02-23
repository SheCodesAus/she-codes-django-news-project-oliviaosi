from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('userProfileStories/', views.UserStoriesView.as_view(), name='userProfileStories'),

]