from django.shortcuts import HttpResponse, render, redirect

from rbac import models
from rbac.service.init_permission import init_permission


def login(request):
    if request.method == 'GET':

        return render(request, 'login.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')

    user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not user:
        return render(request, 'login.html', {'msg': '用户名或密码不正确'})

    init_permission(user, request)

    return redirect('/customer/list/')

