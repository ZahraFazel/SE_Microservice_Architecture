from django.urls import path
from system_patient import views


app_name = "doctor"
urlpatterns = [
    path('signup_patient/', views.signup, name='signup_patient'),
    path('login_patient/', views.login, name='login_patient'),
]
