from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


def index(request):
    # 방법 1
    # return HttpResponseRedirect ('/posts/')

    # 방법 2
    return redirect('posts:post-list')