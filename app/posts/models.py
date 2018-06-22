from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to='post',
        blank=True,
    )
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)


# admin에 등록
# superuser생성
# 로그인해서 post 하나 추가하기