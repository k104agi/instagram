from django.http import HttpResponse
from django.shortcuts import render


# posts.url에서 지정
# config.urls에서는 path('posts/', include('posts.urls'))

# post_list(request)
# -> '/posts/' 식으로

# post_detail(request, pk) <- view parameter 및 path 패턴명에 'pk' 사용
# -> '/posts/3/'

# base.html 기준으로
# TEMPLATE 설정 쓸 것 (templates 폴더를 DIRS에 추가)
# 경로이름은 TEMPLATES_DIR로 settings.py의 윗부분에 추가

# post_list는 'posts/post_list.html'
# post_detail은 'posts/post_detail.html' 사용

# 1. view와 url의 연결 구현
# 2. view에서 template을 렌더링하는 기능 추가
# 3. template에서 QuerySet 또는 object를 사용해서 객체 출력
# 4. template에 extend 사용


def post_list(request):
    # response = 'this is post_list'
    # return render(request, 'posts/post_list.html', context)
    return HttpResponse('Post List')

def post_detail(request, pk):
    # response = 'this is post_detail of'
    # return render(request, 'posts/post_detail.html', response % pk)
    return HttpResponse(f'Post Detail{pk}')