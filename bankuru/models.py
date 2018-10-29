from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.db.models import Count, Sum, Avg, Min, Max


class Debt(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    bank_name = models.CharField("銀行名", max_length=64)
    principal = models.PositiveIntegerField("元本")
    first_payment_date = models.DateField("初回返済日")
    last_payment_date = models.DateField("最終返済日", blank=True)
    first_payment_amount = models.PositiveIntegerField("初回返済額")
    second_payment_amount = models.PositiveIntegerField("二回目返済額")
    payment_terms = models.PositiveIntegerField("返済回数")
    interest = models.FloatField("金利", default=0)
    is_kyokai = models.BooleanField("保証協会あり", default=False)
    is_tanpo = models.BooleanField("担保あり", default=False)
    is_dhosho = models.BooleanField("代表者保証あり", default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bank_name) + '-元本' + str(self.principal) + '-現在残高' + str(self.get_current(0))


    def get_thousand_principal(self):
        thousand_principal = round(self.principal / 1000)
        return thousand_principal

    def get_thousand_monthly1(self):
        thousand_monthly1 = round(self.first_payment_amount / 1000)
        return thousand_monthly1

    def get_thousand_monthly2(self):
        thousand_monthly2 = round(self.second_payment_amount / 1000)
        return thousand_monthly2


    def get_month_value(self):
        y_value = self.first_payment_date.year - 1900 + 1
        m_value = self.first_payment_date.month
        month_value = y_value * 12 + m_value
        return month_value

    
    def get_last_payment_date(self):
        return last_payment_date


    def reverse_month_value(self):
        month = self % 12
        year = self - 1900 - month
        return year, month


    def get_current(self, kagetsu):
        today = timezone.now().date()
        t_year_value = today.year - 1900 +1
        t_month_value = t_year_value * 12 + today.month + kagetsu
        f_month_value = self.get_month_value()       
        X = t_month_value - f_month_value
        if  X < 1:
            current_balance = self.principal
        else:
            current_balance = self.principal - self.first_payment_amount - self.second_payment_amount * X
            if current_balance < 0:
               current_balance = 0
        return current_balance


    def get_current_0(self):
        balance = round(self.get_current(0) / 1000 )
        return balance

    def get_current_1(self):
        balance = round(self.get_current(1) / 1000 )
        return balance

    def get_current_2(self):
        balance = round(self.get_current(2) / 1000 )
        return balance

    def get_current_3(self):
        balance = round(self.get_current(3) / 1000 )
        return balance

    def get_current_4(self):
        balance = round(self.get_current(4) / 1000 )
        return balance

    def get_current_5(self):
        balance = round(self.get_current(5) / 1000 )
        return balance

    def get_current_6(self):
        balance = round(self.get_current(6) / 1000 )
        return balance

    def get_current_7(self):
        balance = round(self.get_current(7) / 1000 )
        return balance

    def get_current_8(self):
        balance = round(self.get_current(8) / 1000 )
        return balance

    def get_current_9(self):
        balance = round(self.get_current(9) / 1000 )
        return balance

    def get_current_10(self):
        balance = round(self.get_current(10) / 1000 )
        return balance

    def get_current_11(self):
        balance = round(self.get_current(11) / 1000 )
        return balance

    def get_current_12(self):
        balance = round(self.get_current(12) / 1000 )
        return balance

    def get_current_24(self):
        balance = round(self.get_current(24) / 1000 )
        return balance

    def get_current_36(self):
        balance = round(self.get_current(36) / 1000 )
        return balance

    def get_current_48(self):
        balance = round(self.get_current(48) / 1000 )
        return balance

    def get_current_60(self):
        balance = round(self.get_current(60) / 1000 )
        return balance


    def get_count(self):
        return self.objects.aggregate(Count('bank_name'))

