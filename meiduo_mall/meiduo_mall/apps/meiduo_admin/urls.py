from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from .views import statistical
urlpatterns = [
    # 登录路由
    url(r'^authorizations/$', obtain_jwt_token),
    # 数据统计
    # 用户数量
    url(r'^statistical/total_count/$', statistical.UserCountView.as_view()),
]
