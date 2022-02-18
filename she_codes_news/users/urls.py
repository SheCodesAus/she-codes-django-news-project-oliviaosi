from django.urls import path
from .views import CreateAccountView
from . import views

app_name = 'users'

urlpatterns = [
    path('userProfile/', views.UserProfileView.as_view(), name='userProfile'),
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    # path('userProfileStories/', views.UserStoriesView.as_view(), name='userProfileStories'),
    # path('<str:username>/', views.Profile.as_view(), name='user_profile'),


]




