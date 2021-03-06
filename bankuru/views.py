from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from .models import Debt, User
from .forms import LoginForm, DebtForm, UserUpdateForm
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count, Sum, Avg, Min, Max

User = get_user_model()


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
 # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じなら許可
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']
 
 
class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'bankuru/user_detail.html'
 
 
class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'bankuru/user_form.html'
 
    def get_success_url(self):
        return resolve_url('bankuru:user_detail', pk=self.kwargs['pk'])


# @login_required
class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        data = Debt.objects.filter(active=True).filter(user = self.request.user).order_by('-first_payment_date')[:5]
        kagetsu = 0
        if data:
            current_total_balance = round(get_current_total_balance(data, kagetsu) / 1000)
            current_total_payment = round(get_current_total_payment(data, kagetsu) / 1000)
            current_total_interest = round(get_current_total_interest(data, kagetsu))
            current_weighted_average_interest = round((current_total_interest
             / (current_total_balance * 1000))*100*12,2)
        else:
            current_total_balance = 0
            current_total_payment = 0
            current_total_interest = 0
            current_weighted_average_interest = 0

        params = {
            "title": 'ダッシュボード',
            "data": data,
            "current_total_balance": current_total_balance,
            "current_total_payment": current_total_payment,
            "current_total_interest": current_total_interest,
            "current_weighted_average_interest": current_weighted_average_interest,
            }
        return render(request, 'bankuru/index.html', params)


class ChartData(APIView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)  

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        def get_data(self):
            return Debt.objects.filter(active=True).filter(user=1)
        # data = Debt.objects.filter(active=True).filter(user = 1)
        kagetsu = 0
        labels = get_chart_label(get_data(self))
        default_items = get_chart_data(get_data(self), kagetsu)
        
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


class DebtListView(LoginRequiredMixin, ListView):
    model = Debt
    paginate_by = 10

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user).filter(active=True).order_by('bank_name')


class DebtDetailView(LoginRequiredMixin, DetailView):
    model = Debt


class DebtCreateView(LoginRequiredMixin, CreateView):
    model = Debt
    # fields = ('bank_name', ) 
    form_class = DebtForm
    # form_class.user = get_user_model()
    # initial={'user': get_initial()}
    success_url = reverse_lazy('bankuru:debt_list')
    template_name = 'bankuru/debt_create_form.html'

    # def get_initial(self):
    #     return {'user': get_user_model()}

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を登録しました'.format(form.instance))
        return result
    

class DebtUpdateView(LoginRequiredMixin, UpdateView):
    model = Debt
    form_class = DebtForm
    success_url = reverse_lazy('bankuru:debt_list')
    template_name = 'bankuru/debt_update_form.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result


class DebtDeleteView(LoginRequiredMixin, DeleteView):
    model = Debt
    form_class = DebtForm
    success_url = reverse_lazy('bankuru:debt_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result


class TermsOfUse(TemplateView):
    template_name = 'terms_of_use.html' 


def get_current_total_balance(data, kagetsu):
    current_total_balance = 0
    for item in data:
        current_total_balance += item.get_current(kagetsu)
    return current_total_balance


def get_current_total_payment(data, kagetsu):
    current_total_payment = 0
    for item in data:
        current_total_payment += item.second_payment_amount
    return current_total_payment


def get_current_total_interest(data, kagetsu):
    current_total_interest = 0
    for item in data:
        current_total_interest += ( item.get_current(kagetsu) * item.interest /100 / 12)
    return current_total_interest


def get_share(data, kagetsu):
    return share

def get_chart_data(data, kagetsu):
    chart_data = []
    for item in data:
        chart_data.append(item.get_current(kagetsu))
    return chart_data


def get_chart_label(data):
    chart_labels = []
    for item in data:
        chart_labels.append(item.bank_name)
    return chart_labels


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'bankuru/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'bankuru/index.html'


def Charts(request):
    return render(request, 'bankuru/charts.html')

    
