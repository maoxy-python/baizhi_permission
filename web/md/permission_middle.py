import re
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class CheckPermission(MiddlewareMixin):
    """
    用户权限信息校验
    """
    def process_request(self, request):
        """
        当用户请求进入时触发执行
        :param request: 请求相关的参数都在request中
        :return:
        """
        """
        1. 获取当前用户请求的url
        2. 获取当前用户在session中保存的权限列表
        3. 权限信息匹配
        4. url白名单，有些路由默认所有人都可以访问
        """
        valid_url_list = [
            '/login/',
            '/admin/.*',
        ]
        # 当前登录用户的url
        current_url = request.path_info

        # 判断当前用户访问的连接是否在白名单中
        for valid_url in valid_url_list:
            if re.match(valid_url, current_url):
                # 白名单中的url不再验证
                return None

        # 获取当前用户在session中的权限信息
        permission_list = request.session.get('BZEdu_permission_key')
        if not permission_list:
            return HttpResponse('未获取到用户的权限信息，请登录')

        flag = False

        # 匹配当前用户要访问的url是否在用户的权限列表中
        for url in permission_list:
            # 使用正则起至终止符匹配路由，保证路由匹配的合理性
            reg = "^%s$" % url
            if re.match(reg, current_url):
                flag = True
                break

        if not flag:
            return HttpResponse('无权访问')
