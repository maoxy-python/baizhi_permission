from django.conf import settings

def init_permission(user, request):
    """
    用户权限的初始化
    :param user: 当前用户对象
    :param request: 请求相关的所有数据
    :return:
    """

    # 2. 根据用户信息获取此用户所拥有的权限，并放入session
    permission_queryset = user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                              "permissions__title",
                                                                              "permissions__menu_id",
                                                                              "permissions__menu__title",
                                                                              "permissions__menu__icon",
                                                                              "permissions__pid",
                                                                              "permissions__url").distinct()

    # 获取权限中所有的URL
    # permission_list = []
    # for item in permission_queryset:
    #     print(item)
    #     permission_list.append(item['permissions__url'])

    # 3. 使用列表生成式获取所有的权限url   获取菜单信息
    # permission_list = [item['permissions__url'] for item in permission_queryset]

    menu_dict = {}

    # menu_list = []
    permission_list = []
    for item in permission_queryset:
        # 为了完成点击默认选中菜单的效果，重新获取了permissions_list, 通过id|pid判断当前点击的菜单是几级菜单
        # 如果是二级菜单 则默认选中其父菜单
        permission_list.append(item['permissions_url'])

        menu_id = item['permissions__menu_id']

        if not menu_id:
            continue

        node = {'id': item['permissions__id'], 'title': item['permissions__title'], 'url': item['permissions__url']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }
        # if item['permissions__is_menu']:
        #     temp = {
        #         'title': item['permissions__title'],
        #         'icon': item['permissions__icon'],
        #         'url': item['permissions__url'],
        #     }
        #     menu_list.append(temp)
        # permission_list.append(item['permissions__url'])

    # 将权限放入session中，下次直接在session中读取
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_dict
