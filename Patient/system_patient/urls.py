from django.urls import path
from system_patient import views


app_name = "patient"
urlpatterns = [
    path('signup_patient/', views.signup, name='signup_patient'),
    path('login_patient/', views.login, name='login_patient'),
    path('validate_with_national_code/', views.validate_with_national_code, name='validate_with_national_code'),
    path('validate_with_token/', views.validate_with_token, name='validate_with_token'),
    path('get_patients/', views.get_patients, name='get_patients'),
    path('get_all_patients/', views.get_all_patients, name='get_all_patients')
]
