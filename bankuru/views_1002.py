from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Debt


# 基本的にClassビューで定義

class IndexView(View):
    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        debt_data = Debt.objects.filter(user=request.user.id).filter(active=True)
        total_current_balance = 0
        chart_data = [1,2,3,4,5,6]
        chart_label = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        
        for item in debt_data:
            total_current_balance += item.get_current()
        
        params = {'title': 'DashBoard',
                'count': debt_data.count,
                'total_current_balance': total_current_balance,
                'debt_data': debt_data,
                'chart_data': chart_data,
                'chart_label': chart_label, 
        }    
        return render(request, 'bankuru/index.html', params)


def DebtList(request):
    today = timezone.now().date()
    data = Debt.objects.filter(user=request.user.id).filter(active=True)
    debt_data = Debt.objects.filter(user=request.user.id).filter(active=True)
    chart_data = get_piechart_data(debt_data)
    chart_label = get_piechart_label(debt_data)

    yokugetsu = today + relativedelta(months=1)
    params = {'data': data,
              'title': '借入一覧',
              'today': today,
              'yokugetsu': yokugetsu,
              'chart_data': chart_data,
              'chart_label': chart_label,
    }
    return render(request, 'bankuru/debtlist.html', params)

def Charts(request):
    return render(request, 'bankuru/charts.html')

# 普通の関数
def get_data(request, *args, **kwargs):
    data = {
        "sales": [100,2],
        "customers": ['red','blue'],
    }
    return JsonResponse(data)


def get_piechart_data(data):
    chartdata = [100,111,120]
    return chartdata

def get_piechart_label(data):
    chartlabel = ['みずほ', 'SMBC', '三菱']
    return chartlabel

    
