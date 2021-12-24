from django.urls import path
from system_doctor import views


app_name = "doctor"
urlpatterns = [
    path('signup_doctor/', views.signup, name='signup_doctor'),
    path('login_doctor/', views.login, name='login_doctor'),
    path('validate_with_token/', views.validate_with_token, name='validate_with_token'),
    path('get_doctors/', views.get_doctors, name='get_doctors')
]
