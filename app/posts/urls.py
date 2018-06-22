from django.urls import path
from posts import views

app_name = 'posts'

# config.urls
# path('posts/', include(이 urlpatterns)) 이하 경로를 만들면 됨

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_detail),
]