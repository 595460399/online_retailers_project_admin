from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    #登录路由
    url(r'^authorizations/$', obtain_jwt_token),
]
