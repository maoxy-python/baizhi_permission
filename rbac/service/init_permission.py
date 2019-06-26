

def init_permission(user, request):
    """
    用户权限的初始化
    :param user: 当前用户对象
    :param request: 请求相关的所有数据
    :return:
    """

    # 根据用户信息获取此用户所拥有的权限，并放入session
    permission_queryset = user.roles.filter(permissions__isnull=False).values("permissions__id", "permissions__url").distinct()

    # 获取权限中所有的URL
    # permission_list = []
    # for item in permission_queryset:
    #     print(item)
    #     permission_list.append(item['permissions__url'])

    # 使用列表生成式获取所有的权限url
    permission_list = [item['permissions__url'] for item in permission_queryset]

    # 将权限放入session中，下次直接在session中读取
    request.session['BZEdu_permission_key'] = permission_list