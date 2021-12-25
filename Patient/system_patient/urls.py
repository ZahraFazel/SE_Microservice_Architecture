from django.urls import path
from system_patient import views


app_name = "patient"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('validate_with_national_code/', views.validate_with_national_code, name='validate_with_national_code'),
    path('validate_with_token/', views.validate_with_token, name='validate_with_token'),
    path('get_patients/', views.get_patients, name='get_patients'),
    path('get_all_patients/', views.get_all_patients, name='get_all_patients'),
    path('get_new_patients/', views.get_new_patients, name='get_new_patients'),
    path('profile/', views.profile, name='profile')
]
