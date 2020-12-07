from django.shortcuts import render
from django.http import HttpResponse
from users.models import User

# /register/
def register(request):
    """注册View视图函数"""
    # 注册页面内容
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(f'username:{username}password:{password}')
        user = User.objects.create(username=username, password=password)

        # 返回响应
        return HttpResponse('注册成功')
# Create your views here.
