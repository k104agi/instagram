from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    # 1. member.urls <- 'members/'로 include 되도록 config.urls 모듈에 추가
    # 2. path 구현 (URL:'/members/login/')
    # 3. path와 이 view 연결
    # 4. 잘 나오는지 먼저 확인
    # 5. 잘 나오면 form을 작성 (username, password를 받는 input 2개)
    # templates/members/login.html

    # 6.form 작성 후에는 POST 방식 요청을 보내서이 뷰에서 request.POST에 요청이 잘 왔는지 확인
    # 7. 일단은 받은 username, passwords 값을 HttpResponse에 보여주도록 한다.
    # username = request.POST['username']
    # passwords = request.POST['password']
    # return HttpResponse('login_view')
    # print(request.POST)
    # runserver 창에서 볼 수 있음

    # return render(request, 'members/login.html')

    # print(f'{username}, {password}')

    # 인증에 성공하면 posts:post-list로 이동
    # 실패하면 다시 members:login으로 이동
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:post-list')
        else:
            return redirect('members:members-login')
    else:
        return render(request, 'members/login.html')
