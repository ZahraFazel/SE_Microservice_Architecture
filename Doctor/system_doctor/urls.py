from django.urls import path, include
from system_doctor import views


app_name = "doctor"
urlpatterns = [
    path('signup_doctor/', views.signup_doctor, name='signup_doctor'),
    path('login_doctor/', views.login_doctor, name='login_doctor'),
]
