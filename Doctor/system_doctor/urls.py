from django.urls import path
from system_doctor import views

app_name = "doctor"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('validate_with_token/', views.validate_with_token, name='validate_with_token'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_all_doctors/', views.get_all_doctors, name='get_all_doctors'),
    path('get_new_doctors/', views.get_new_doctors, name='get_new_doctors'),
    path('profile/', views.profile, name='profile')
]
