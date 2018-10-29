from django import forms
from .models import Debt, User
from django.contrib.auth.forms import (
    AuthenticationForm
)
 
 
class LoginForm(AuthenticationForm):
    """ログインフォーム"""
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['user', 'bank_name','principal','first_payment_date',
        'last_payment_date','first_payment_amount',
        'second_payment_amount','payment_terms','interest' ]
        
        
class UserUpdateForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserCreateForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')