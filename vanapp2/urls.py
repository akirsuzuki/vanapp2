from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bankuru/', include('bankuru.urls')),
    path('admin/', admin.site.urls),
]
