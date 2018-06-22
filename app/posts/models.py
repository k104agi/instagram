from django.conf import settings
from django.db import models

'''
POST 클래스 추가, MEDIA_URL 연결

MEDIA_ROOT는 실제 파일이 업로드되는 기준 경로
MEDIA_URL은 사용자가 업로드한 파일을 제공할 URL
config.urls에 추가한 static()은 MEDIA_URL로의 request에 대해
MEDIA_ROOT에서 찾은 파일을 response로 돌려줌

'''

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