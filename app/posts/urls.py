from django.urls import path
from posts import views

app_name = 'posts'

# config.urls
# path('posts/', include(이 urlpatterns)) 이하 경로를 만들면 됨

urlpatterns = [
    # localhost:8000/posts
    path('', views.post_list, name='post-list'),

    # localhost:8000/posts/1
    path('<int:pk>', views.post_detail, name='post-detail'),
]