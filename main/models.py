from django.db import models

class Users(models.Model):
    title = models.CharField(max_length=75)
    img = models.URLField(max_length=200)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    data_posted = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
