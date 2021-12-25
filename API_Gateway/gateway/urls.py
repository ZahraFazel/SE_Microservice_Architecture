from django.views.generic import RedirectView
from django.urls import path, include

from API_Gateway.settings import ADMIN_URL, DOCTOR_URL, PATIENT_URL, DB_AGGREGATOR_URL, PRESCRIPTION_URL
from gateway import views


app_name = "gateway"
urlpatterns = [
    path('login_admin/', views.login_admin),
    path('signup_doctor/', views.signup_doctor),
    path('login_doctor/', views.login_doctor),
    path('signup_patient/', views.signup_patient),
    path('login_patient/', views.login_patient),
    path('prescript/', views.prescript),
    path('list_patient_prescriptions/', views.list_patient_prescriptions),
    path('list_doctor_prescriptions/', views.list_doctor_prescriptions),
    path('list_prescriptions/', views.list_prescriptions),
    path('list_doctors/', views.list_doctors),
    path('list_patients/', views.list_patients),
    path('get_daily_statistics/', views.get_daily_statistics),
    path('get_admin_profile/', views.get_admin_profile),
    path('get_doctor_profile/', views.get_doctor_profile),
    path('get_patient_profile/', views.get_patient_profile),
]
