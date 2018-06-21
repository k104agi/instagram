from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField()
    content = models.TextField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
