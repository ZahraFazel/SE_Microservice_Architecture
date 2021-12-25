from django.urls import path
from administrator import views


app_name = "my_admin"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('validate_with_token/', views.validate_with_token, name='validate_with_token'),
    path('profile/', views.profile, name='profile')
]
