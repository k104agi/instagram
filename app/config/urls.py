"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

'''
POST 클래스 추가, MEDIA_URL 연결

MEDIA_ROOT는 실제 파일이 업로드되는 기준 경로
MEDIA_URL은 사용자가 업로드한 파일을 제공할 URL
config.urls에 추가한 static()은 MEDIA_URL로의 request에 대해
MEDIA_ROOT에서 찾은 파일을 response로 돌려줌

'''
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', views.index),
    # path('media/<str:path>/',특정view_function추가),
    # 위 기능을 요약한 장고기능이 있음 - 하단 + static
] + static(
    prefix =settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
