from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Meme(models.Model):
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to="meme_pics")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)
    data_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height > 600 or img.width > 600:
    #         output_size = (600, 600)
    #         img.thumbnail(output_size)

