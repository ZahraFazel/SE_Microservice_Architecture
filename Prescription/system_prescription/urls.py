from django.views.generic import RedirectView
from django.urls import path, include
from system_prescription import views


app_name = "prescription"
urlpatterns = [
    path('new_prescription/', views.new_prescription, name='new_prescription'),
]
