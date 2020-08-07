from django.db import models
from django.contrib.auth.models import User

class Meme(models.Model):
    title = models.CharField(max_length=75)
    img = models.URLField(max_length=200)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)
    data_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


# class Users(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=50)
#     favorites = models.ForeignKey("Meme", on_delete=models.CASCADE)