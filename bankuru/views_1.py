from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from .models import Debt

# ビュー関数

def Index(request):
    today = timezone.now().date()
    t_month_value = get_month_value(today.year, today.month)
    data = Debt.objects.filter(user=request.user.id).filter(active=True)
    updated_data = update_current(data, t_month_value)
    total_current_balance = (sum_current(data) / 1000).round

    params = {'title': 'DashBoard',
              'today': today,
              'count': data.count,
              't_month_value': t_month_value,
              'updated_data': updated_data,
              'total_current_balance': total_current_balance,
    }    
    return render(request, 'bankuru/index.html', params)

def DebtList(request):
    today = timezone.now().date()
    data = Debt.objects.filter(user=request.user.id).filter(active=True)

    yokugetsu = today + relativedelta(months=1)
    params = {'data': data,
              'title': '借入一覧',
              'today': today,
              'yokugetsu': yokugetsu,
    }
    return render(request, 'bankuru/debtlist.html', params)
  



# 普通の関数

def get_month_value(year, month):
    y_value = year - 1900 + 1
    m_value = month
    month_value = y_value * 12 + m_value
    return month_value

def update_current(data, month_value):
    for item in data:
        item.last_payment_date = item.first_payment_date + relativedelta(months=item.count - 1)
        current_interest = 0
        t_month_value = month_value
        f_month_value = get_month_value(item.first_payment_date.year, item.first_payment_date.month)
        X = t_month_value - f_month_value
        if  X < 1:
            item.current_balance = item.principal
            item.save()
        else:
            item.current_balance = item.principal - item.first_payment_amount - item.second_payment_amount * X
            if item.current_balance < 0:
                item.current_balance = 0
                item.save()
            else:
                item.save()
    return data

def sum_current(data):
    sum = 0
    for item in data:
        sum += item.current_balance
    return sum
    
