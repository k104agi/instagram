from django.contrib import admin

from .models import Post

# app.posts.models = .models (.는 현재경로니까 apps가 있는 레벨 = models랑 같은 레벨)

admin.site.register(Post)
