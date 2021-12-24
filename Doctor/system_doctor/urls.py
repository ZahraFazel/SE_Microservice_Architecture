from django.urls import path
from system_doctor import views


app_name = "doctor"
urlpatterns = [
    path('signup_doctor/', views.signup, name='signup_doctor'),
    path('login_doctor/', views.login, name='login_doctor'),
    path('validate/', views.validate, name='validate')
]
