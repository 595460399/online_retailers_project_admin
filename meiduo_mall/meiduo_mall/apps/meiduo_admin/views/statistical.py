from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from datetime import date, timedelta

from goods.models import GoodsVisitCount
from meiduo_admin.serialziers.statistical import UserGoodsCountSerializer
from users.models import User


def UserCountView(APIView):
    """
    用户统计视图
    """
    # 权限指定
    permission_class = [IsAdminUser]

    def get(self, request):
        # 获取当天时间
        now_day = date.today()
        # 获取用户总量
        count = User.objects.all().count()
        # 返回结果
        return Response({
            'date': now_day,
            'count': count,
        })


def UserDayCountView(APIView):
    """
    日增用户统计视图
    """
    # 权限指定
    permission_class = [IsAdminUser]

    def get(self, request):
        # 获取当天时间
        now_day = date.today()
        # 获取用户日增量
        count = User.objects.filter(date_joined__day__gte=now_day).count()
        # 返回结果
        return Response({
            'date': now_day,
            'count': count,
        })


class UserActiveCountView(APIView):
    """
    日活躍用戶統計
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取当日登录用户数量  last_login记录最后登录时间
        count = User.objects.filter(last_login__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserOrderCountView(APIView):
    '''
    下單用戶統計
    '''
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取当日下单用户数量  orders__create_time 订单创建时间
        count = User.objects.filter(orders__create_time__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserMonthCountView(APIView):
    """
    統計每月每天的新增用戶量
    從當天時間算起前一個月
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取一个月前日期
        start_date = now_date - timedelta(29)
        # 创建空列表保存每天的用户量
        date_list = []

        for i in range(30):
            # 循环遍历获取当天日期
            index_date = start_date + timedelta(days=i)
            # 指定下一天日期
            cur_date = start_date + timedelta(days=i + 1)
            # 查询条件是大于当前日期index_date，小于明天日期的用户cur_date，得到当天用户量
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=cur_date).count()

            date_list.append({
                'count': count,
                'date': index_date
            })

            return Response(date_list)


class UserGoodsCountView(APIView):
    '''
    獲取當天訪問量數量
    '''
    def get(self, request):
        # 获取当天日期
        now_date = date.today()
        # 获取当天访问的商品分类数量信息
        goods = GoodsVisitCount.objects.filter(date=now_date)
        # 序列化返回分类数量
        ser = UserGoodsCountSerializer(goods, many=True)

        return Response(ser.data)
