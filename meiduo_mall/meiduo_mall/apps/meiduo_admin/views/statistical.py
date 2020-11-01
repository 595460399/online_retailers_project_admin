from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from datetime import date
from users.models import User
def UserCountView(APIView):
    """
    用户统计视图
    """
    # 权限指定
    permission_class = [IsAdminUser]

    def get(self, request):
        #获取当天时间
        now_day = date.today()
        #获取用户总量
        count = User.objects.all().count()
        #返回结果
        return Response({
            'date':now_day,
            'count':count,
        })
