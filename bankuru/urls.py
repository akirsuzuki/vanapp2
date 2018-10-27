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
    # path('user_create', views.UserCreate.as_view(), name='user_create'),
    # path('contact_us', views.ContactUs, name='contact_us'),
    # path('contact_us_vendor', views.ContactUsVendor, name='contact_us_vendor'),
    # path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    # path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    # path('product_detail/<str:product_name_url>', views.ProductDetail, name='product_detail'),
    # path('company/<str:company_name_url>', views.CompanyDetail, name='company_detail'),
    # path('review_create/<str:product_name_url>', views.ReviewCreate, name='review_create'),
    # path('review_edit/<int:num>', views.ReviewEdit, name='review_edit'),
    # path('review_delete/<int:num>', views.ReviewDelete, name='review_delete'),
    # path('product_reviews/<str:product_name_url>', views.ProductReviews, name='product_reviews'),
    # path('blog/', views.BlogIndex, name='blog_index'),
    # path('blog_detail/<int:blog_id>', views.BlogDetail, name='blog_detail'),
    # path('<str:user_name>', views.MyPage, name='mypage'),
    # path('user_edit/<str:user_name>', views.UserEdit, name='user_edit'),
    # path('category/<str:category_name_url>', views.CategoryIndex, name='category'),
]