from django.urls import re_path

from web.views import customer
from web.views import payment
from web.views import account

urlpatterns = [

    re_path(r'^customer/list/$', customer.customer_list),
    re_path(r'^customer/add/$', customer.customer_add),
    re_path(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit),
    re_path(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del),
    re_path(r'^customer/import/$', customer.customer_import),
    re_path(r'^customer/tpl/$', customer.customer_tpl),

    re_path(r'^payment/list/$', payment.payment_list),
    re_path(r'^payment/add/$', payment.payment_add),
    re_path(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit),
    re_path(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del),

    re_path(r'^login/$', account.login)

]
