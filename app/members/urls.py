from django.urls import path
from members import views

app_name = 'members'

urlpatterns = [
    # localhost:8000/posts
    path('login/', views.login_view, name='members-login'),
    path('logout/',views.logout_view, name='members-logout')
]
