from django.contrib.auth import get_user_model

from django.db import models 

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author= models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    pub_date = models.DateTimeField()
    content = models.TextField()
    image= models.URLField(blank=True,null= True)

class NewAuthor(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
   


