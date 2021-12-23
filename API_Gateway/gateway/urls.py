from django.views.generic import RedirectView
from django.urls import path, include

from API_Gateway.settings import ADMIN_URL
from gateway import views


app_name = "gateway"
urlpatterns = [
    path('login_admin/', views.login_admin),
    path('signup_doctor/', views.signup_doctor),
    path('login_doctor/', views.login_doctor),
]
