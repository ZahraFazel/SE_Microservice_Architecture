from django.urls import path, include
from administrator import views


app_name = "my_admin"
urlpatterns = [
    path('login_admin/', views.login_admin, name='login_admin'),
    path('validate_with_token/', views.validate_with_token, name='validate_with_token'),
]
