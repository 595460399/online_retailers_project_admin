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
    #日增用户统计
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    #日活跃用户统计
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    #日下单用户量统计
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),
    #月日增用户统计
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    #日分类商品访问量
    url(r'^statistical/goods_day_views/$', statistical.UserCountView.as_view()),
]
