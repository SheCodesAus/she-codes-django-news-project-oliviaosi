from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('userProfile/', views.UserProfileView.as_view(), name='userProfile'),

]




