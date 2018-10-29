from django.urls import path

from . import views
from .views import IndexView, ChartData, TermsOfUse

app_name = 'bankuru'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/chart/data', ChartData.as_view(), name='chart-data'),
    path('debt_list', views.DebtListView.as_view(), name='debt_list'),
    path('debt_detail/<int:pk>', views.DebtDetailView.as_view(), name='debt_detail'),
    path('debt_form', views.DebtCreateView.as_view(), name='debt_create'),
    path('debt_update/<int:pk>', views.DebtUpdateView.as_view(), name='debt_update'),
    path('debt_delete/<int:pk>', views.DebtDeleteView.as_view(), name='debt_delete'),
    path('charts', views.Charts, name='charts'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('terms_of_use', views.TermsOfUse.as_view(), name='terms_of_use'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]