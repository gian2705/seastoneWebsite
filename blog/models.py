from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    user_post = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True, default=1)
    title = models.CharField(max_length=128)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
